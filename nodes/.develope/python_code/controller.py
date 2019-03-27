import socket
import time
import json
import sys
import argparse
import gevent

from gevent import monkey

monkey.patch_all()

def test(s):
    while(True):
        recv = s.recv(1024).decode()
        if(recv == "[STATUS] : Sensing finished..."):
            s.close()
            break
        print(recv)

def run(experiment_type):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
    current_time = float('%.3f'%time.time())
    start_time = '%.3f'%(round(current_time,2)+2)
    end_time = '%.3f'%(round(current_time,2)+5)

    node1 = '192.168.1.207' #node's ip address / raspberry ip
    node3 = '192.168.1.54' #node's ip address / raspberry ip
    port = 4000

    try:
        s2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s1.connect((node1, port))
        s2.connect((node3, port))
    except Exception as e:
        print("[ERROR] : Remote Node Program Connection Failed")
        s2.close()
        sys.exit(1)
    attr = ['Test_file_name',start_time,end_time,experiment_type]
    print("[INFO] : Experiment type <"+experiment_type+"> starts...")
    print("[INFO] : Nodes will start at ("+ str(start_time)+") and terminates at ("+str(end_time)+")")
    data = json.dumps({"attr":attr})
    s1.sendall(data.encode()) # signal to start sensing
    s2.sendall(data.encode()) # signal to start sensing
    #while(True):
    try:
        jobs = [gevent.spawn(test,_s) for _s in [s1,s2]]
        gevent.wait(jobs)
        '''
        recv = s1.recv(1024).decode()
        #condition to terminate connection
        if(recv == "[STATUS] : Sensing finished..."):
            raise KeyboardInterrupt
        print(recv)
        '''

    except (KeyboardInterrupt, EOFError) as e:
        print("[STATUS] : Control Program finishing....")
        s2.close()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Controller for experiment')

    parser.add_argument('-t','--type',help='-t [EXPERIMENT_TYPE]',required=True)
    args = parser.parse_args()

    run(args.type)
    

import socket
import time
import json
import sys
import argparse
import gevent
from termcolor import colored 

from gevent import monkey

monkey.patch_all()

OPTION = 3 #0 or 3 //excluding 3 node or not

def test(s):
    while(True):
        recv = s.recv(1024).decode()
        if(recv[0:7] == "[ERROR]"):
            s.close()
            print(colored(recv[:7],'red',attrs=['bold','reverse'])+recv[8:])
            break
        if(recv == "[STATUS] : Sensing finished..."):
            s.close()
            break
        print(recv)

def run(experiment_type,duration,file_name):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
    current_time = float('%.3f'%time.time())
    start_time = '%.3f'%(round(current_time,2)+3)
    end_time = '%.3f'%(round(current_time,2)+duration+2)

    node1 = '192.168.1.207' #node's ip address / raspberry ip
    node2 = '192.168.1.220' #node's ip address / raspberry ip
    node3 = '192.168.1.54' #node's ip address / raspberry ip
    node4 = '192.168.1.187' #node's ip address / raspberry ip
    port = 4000

    try:
        s2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s3 = None
        if OPTION == 3:
            s3 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s4 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s1.connect((node1, port))
        s2.connect((node2, port))
        if not s3 == None: 
            s3.connect((node3, port))
        s4.connect((node4, port))                           ##socket connection
    except Exception as e:
        print("[ERROR] : Remote Node Program Connection Failed")
        s2.close()
        if not s3 == None: 
            s3.close()
        s4.close()                                          ##socket close
        sys.exit(1)
    attr = [file_name,start_time,end_time,experiment_type]
    print("[INFO] : Experiment type <"+experiment_type+"> starts at "+str(time.time()))
    print("[INFO] : Nodes will start at ("+ str(start_time)+") and terminates at ("+str(end_time)+")")
    data = json.dumps({"attr":attr})

    s1.sendall(data.encode()) # signal to start sensing
    s2.sendall(data.encode()) # signal to start sensing
    if not s3 == None: 
        s3.sendall(data.encode()) # signal to start sensing
    s4.sendall(data.encode()) # signal to start sensing     

    try:
        if not s3 == None: 
            jobs = [gevent.spawn(test,_s) for _s in [s1,s2,s3,s4]]
        else:
            jobs = [gevent.spawn(test,_s) for _s in [s1,s2,s4]]
        gevent.wait(jobs)

    except (KeyboardInterrupt, EOFError) as e:
        print("[STATUS] : Control Program finishing by ctrl-c....")
        s2.close()
        if not s3 == None: 
            s3.close()
        s4.close()                                          ##socket close
    finally:
        print("[STATUS] : Control Program finishing....")
        s2.close()
        if not s3 == None: 
            s3.close()
        s4.close()                                          ##socket close

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Controller for experiment')

    parser.add_argument('-f','--file',help='-f [SAVE_FILE_NAME]',required=True)
    parser.add_argument('-t','--type',help='-t [EXPERIMENT_TYPE]',required=True)
    parser.add_argument('-d','--duration',help='-d [EXPERIMENT_TYPE_DURATION_TIME]',required=True)
    args = parser.parse_args()

    run(args.type,int(args.duration),args.file)
    

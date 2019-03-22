import socket
import time
import json
import sys

def run():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    current_time = float('%.3f'%time.time())
    start_time = '%.3f'%(round(current_time,2)+2)
    end_time = '%.3f'%(round(current_time,2)+5)

    node1 = '192.168.1.207' #node's ip address / raspberry ip
    host = node1
    port = 4000
    try:
        s.connect((host, port))
    except Exception as e:
        print("[ERROR] : Remote Node Program Connection Failed")
        sys.exit(1)
    attr = ['first_file_name',start_time,end_time,'collision case1']
    print("[data] : "+ str(current_time))
    print("[data] : "+ str(attr))
    data = json.dumps({"attr":attr})
    s.sendall(data.encode()) # signal to start sensing
    while(True):
        try:
            recv = s.recv(1024)
            if(recv.decode() == "[STATUS] : Sensing finished..."):
                raise KeyboardInterrupt
            print(recv.decode())
        except (KeyboardInterrupt, EOFError) as e:
            print("[STATUS] : Control Program finishing....")
            sys.exit(1)


    #resp = s.recv(1024)
    #print(resp.decode())

if __name__ == '__main__':
    run()

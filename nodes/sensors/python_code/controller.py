import socket
import time
import json
import sys

def run():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    current_time = '%.3f'%time.time()
    host = '192.168.1.207' #node's ip address / raspberry ip
    port = 4000
    s.connect((host, port))
    attr = ['script_name',123456,123456,'timing']
    data = json.dumps({"attr":attr})
    s.sendall(data.encode()) # signal to start sensing
    while(True):
        try:
            recv = s.recv(1024)
            print(recv.decode())
        except (KeyboardInterrupt, EOFError) as e:
            print("quit----")
            sys.exit(1)


    #resp = s.recv(1024)
    #print(resp.decode())

if __name__ == '__main__':
    run()

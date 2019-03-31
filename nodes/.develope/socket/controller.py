import socket
import time
import json

def run():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    timing = '%.3f'%time.time()
    host = '127.0.0.1'
    port = 4000
    s.connect((host, port))
    #line = input('>>')
    #time_1 = time.time()
    #line += ('\nsending_time >> '+ str(time_1))
    attr = ['script_name',123456,123456,timing]
    data = json.dumps({"attr":attr})
    s.sendall(data.encode())
    #resp = s.recv(1024)
    #print(resp.decode())

if __name__ == '__main__':
  run()

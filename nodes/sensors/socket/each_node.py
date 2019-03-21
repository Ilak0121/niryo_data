import socket
import time
import sys
import socket
import json

def run_server(port=4000):
  host = '127.0.0.1'
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      try:
          s.bind((host, port))
          s.listen(1)
          while(True):
              conn, addr = s.accept()
              data = conn.recv(1024)
              data = json.loads(data.decode())
              recv_time = float('%.3f'%time.time())
              #time_recv = time.time()
              #print(msg.decode() +'\nreceiving_time >> '+ str(time_recv))
              print(data.get("attr"))
              print('time gap : '+str(recv_time - float(data.get('attr')[3])))
              #conn.sendall(msg)
      except (KeyboardInterrupt, EOFError) as e:
          print('quit----')
          sys.exit(1)

      except Exception as e:
          print(e)
          sys.exit(1)

if __name__ == '__main__':
  run_server()



import os.path
import re
import sys
import time
import socket
import json

from ina219 import (INA219, DeviceRangeError)
from sensingfinished import SensingFinished

SHUNT_OHMS = 0.1

DEBUG_MODE = 0                                      #save file or print monitor

def sensing(chunk,conn):

    #need to accurate
    ina1 = INA219(SHUNT_OHMS,address=0x40)
    ina2 = INA219(SHUNT_OHMS,address=0x41)
    ina3 = INA219(SHUNT_OHMS,address=0x44)
    #
    ina1.configure()
    ina2.configure()
    ina3.configure()

    #received data extraction
    (file_path, start_time, end_time, experiment_type) = chunk 
    p = re.compile('0$') #10ms is the period

    save_txt = ''
    #### first loop for synchronization with each nodes
    while(True): 
        current_time = '%.3f'%time.time()
        if current_time == start_time:
            break

    conn.sendall(("[STATUS] : Node2 program starts as type of "+experiment_type+"....").encode())

    ###sensing starts
    while(True): 
        try:
            end_confirm = string = '%.3f'%time.time()

            if not re.search(r'0$', string) == None:
                string += ',%.4f'%ina1.current()
                string += ',%.4f'%ina2.current()
                string += ',%.4f'%ina3.current()

                if DEBUG_MODE == 1:
                    print(string)
                else:
                    save_txt += string + '\n'                   ###overflow considering after experiment

                if end_confirm == end_time: ## To make the program end and save file
                    raise SensingFinished

        ### Exception handler
        except DeviceRangeError as e:
            print(e)
            conn.sendall(("[DEBUG] : ina219 deviceRangeError occured," + e).encode())
            conn.sendall("[ERROR] : Node2 program terminating....".encode())
            sys.exit(1)

        except (KeyboardInterrupt,EOFError):
            if DEBUG_MODE == 0:
                #path = file_path #'./test.txt'
                with open(file_path,'w') as fd:
                    #fd.write('%s %s \n' % (args.timestamp, args.name)) #meta-data for files
                    fd.write(save_txt) #sensor data
            conn.sendall("[DEBUG] : Node2 program finishing with ctrl-c....".encode())
            break

        except SensingFinished:  #exception should be making
            if DEBUG_MODE == 0:
                #path = file_path #'./test.txt'
                with open(file_path,'w') as fd:
                    #fd.write('%s %s \n' % (args.timestamp, args.name)) #meta-data for files
                    fd.write(save_txt) #sensor data
            conn.sendall("[STATUS] : Node2 Sensing program finishing completely....".encode())
            break

if __name__ == "__main__":

    # node's ip address (raspi)
    node1 = '192.168.1.207' 
    node2 = '192.168.1.220' 
    node3 = '192.168.1.54' 

    host = node2
    port = 4000

    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        try:
            try:
                s.bind((host,port))
                s.listen(1)
            except Exception as e:
                print("[DEBUG] : Bind & Listening error, port number confirm or wait for socket arrange")
                sys.exit(1)

            print("[STATUS] : Node2 program starting...")

            while(True):
                conn, addr = s.accept()
                conn.sendall("[STATUS] : Node2 socket connection established...".encode())

                data = conn.recv(1024)
                data = json.loads(data.decode())

                sensing(data.get('attr'),conn) #processing
                time.sleep(0.5)

                conn.sendall("[STATUS] : Sensing finished...".encode()) #key data to finish

        except (KeyboardInterrupt, EOFError) as e: #ctrl-c let program terminating
            print("[STATUS] : Node2 program finishing...")
            sys.exit(1)

        except Exception as e:
            conn.sendall("[ERROR] : Node2 program unexpected exception event occur!!".encode())
            time.sleep(0.1)
            conn.sendall("[ERROR] : Node2 program terminating....".encode())
            print(e)
            sys.exit(1)


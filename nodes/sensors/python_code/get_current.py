import os.path
import re
import sys
import time
import socket

from ina219 import (INA219, DeviceRangeError)

SHUNT_OHMS = 0.1

DEBUG_MODE = 0                                      #save file or print monitor

def sensing(chunk,conn):

    #need to accurate
    ina1 = INA219(SHUNT_OHMS,address=0x40)
    #ina2 = INA219(SHUNT_OHMS,address=0x41)
    #ina3 = INA219(SHUNT_OHMS,address=0x42)
    ina1.configure()
    #ina2.configure()
    #ina3.configure()

    #received data extraction
    (file_path, start_time, end_time, experiment_type) = chunk 

    p = re.compile('0$') #10ms is the period

    #print("shunt_voltage:%.3f mA"%ina.shunt_voltage())
    #print("bus voltage:%.3f mA"%ina.voltage())

    save_txt = ''
    while(True): 
        #### first loop for synchronization with each nodes
        current_time = '%.3f'%time.time()
        if current_time == start_time:
            break

    while(True): 
        ###sensing starts
        try:
            string = '%.3f'%time.time()
            if string == end_time:                              ### need to check for accurate activation!!!!!!
                raise KeyboardInterrupt 
                ## To make the program end and save file

            if not re.search(r'0$', string) == None:
                string += ","
                string += '%.4f'%ina1.current()

                if DEBUG_MODE == 1:
                    print(string)
                else:
                    save_txt += string + '\n'                   ###overflow considering after experiment

        ### Exception handler
        except DeviceRangeError as e:
            print(e)
            conn.sendall(("[DEBUG] : ina219 deviceRangeError occured," + e).encode())
            conn.sendall("[ERROR] : sensing program terminating....".encode())
            sys.exit(1)

        except (KeyboardInterrupt,EOFError):
            #print("avg"+str(time_avg/n))
            if DEBUG_MODE == 0:
                #path = file_path #'./test.txt'
                with open(file_path,'w') as fd:
                    #fd.write('%s %s \n' % (args.timestamp, args.name)) #meta-data for files
                    fd.write(save_txt) #sensor data
            sys.exit(1)


if __name__ == "__main__":

    host = '127.0.0.1' # node's ip address (raspi)
    port = 4000

    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        try:
            s.bind((host,port))
            s.listen(1)

            while(True):
                conn, addr = s.accept()
                conn.sendall("[STATUS] : socket listening...".encode())

                data = conn.recv(1024)
                data = json.loads(data.decode())

                #sensing(data.get('attr'),conn) #processing

                conn.sendall("[STATUS] : Sensing program has finished...".encode())

        except (KeyboardInterrupt, EOFError) as e: #ctrl-c let program terminating
            sys.exit(1)

        except Exception as e:
            conn.sendall("[ERROR] : Sensing program exception event occur!!".encode())
            conn.sendall("[ERROR] : sensing program terminating....".encode())
            print(e)
            sys.exit(1)


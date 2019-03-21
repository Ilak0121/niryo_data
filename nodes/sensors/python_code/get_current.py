import os.path
import re
import sys
import time
import socket
import argparse

from ina219 import (INA219, DeviceRangeError)

SHUNT_OHMS = 0.1

DEBUG_MODE = 0                                      #save file or print monitor

def sensing(chunk,conn):

    ina = INA219(SHUNT_OHMS)                        #need to accurate
    ina.configure()

    #received data extraction
    (file_path, start_time, end_time, experiment_type) = chunk 

    p = re.compile('0$') #10ms is the period

    #print("shunt_voltage:%.3f mA"%ina.shunt_voltage())
    #print("bus voltage:%.3f mA"%ina.voltage())

    save_txt = ''
    while(True): 
        #### first loop for synchronization with each nodes
        try:
            current_time = '%.3f'%time.time()
            if current_time == start_time:
                break
        except Exception as e:
            print(e)
            conn.sendall("[DEBUG] : time sync waiting loop error occured")
            conn.sendall("[ERROR] : sensing program terminating....")
            sys.exit(1)

        ###sensing starts
        try:
            string = '%.3f'%time.time()
            if string == end_time:                              ### need to check for accurate activation!!!!!!
                raise KeyboardInterrupt 
                ## To make the program end and save file

            if not re.search(r'0$', string) == None:
                string += ","
                string += '%.4f'%ina.current()

                if DEBUG_MODE == 1:
                    print(string)
                else:
                    save_txt += string + '\n'                   ###overflow considering after experiment

        ### Exception handler
        except DeviceRangeError as e:
            print(e)
            conn.sendall("[DEBUG] : ina219 deviceRangeError occured," + e)
            conn.sendall("[ERROR] : sensing program terminating....")
            sys.exit(1)

        except (KeyboardInterrupt,EOFError):
            #print("avg"+str(time_avg/n))
            if DEBUG_MODE == 0:
                #path = file_path #'./test.txt'
                with open(file_path,'w') as fd:
                    #fd.write('%s %s \n' % (args.timestamp, args.name)) #meta-data for files
                    fd.write(save_txt)
            sys.exit(1)


if __name__ == "__main__":

    host = '127.0.0.1' #for socket
    port = 4000

    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        try:
            s.bind((host,port))
            s.listen(1)

            while(True):
                conn, addr = s.accept()
                conn.sendall("[STATUS] : socket listening...")

                data = conn.recv(1024)
                data = json.loads(data.decode())

                sensing(data.get('attr'),conn) #processing

                conn.sendall("[STATUS] : Sensing program has finished...")

        except (KeyboardInterrupt, EOFError) as e: #ctrl-c let program terminating
            sys.exit(1)

        except Exception as e:
            conn.sendall("[ERROR] : Sensing program exception event occur!!")
            conn.sendall("[ERROR] : sensing program terminating....")
            print(e)
            sys.exit(1)


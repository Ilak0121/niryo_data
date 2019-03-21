import os.path
import re
import sys
import time
import socket
import argparse

from ina219 import (INA219, DeviceRangeError)

SHUNT_OHMS = 0.1

DEBUG_MODE = 0 #save file or print monitor

def sensing(name, start, end):
    ina = INA219(SHUNT_OHMS) #need to accurate
    ina.configure()

    p = re.compile('0$')

    #print("shunt_voltage:%.3f mA"%ina.shunt_voltage())
    #print("bus voltage:%.3f mA"%ina.voltage())

    time_avg=0
    n=0
    txt = ''
    while(True): #sensing process
        try:
            string = '%.3f'%time.time()
            if not re.search(r'0$', string) == None:
                string += ","
                #time1 = time.time()
                string += '%.4f'%ina.current()
                #time2 = time.time()
                #if args.save == False:
                if DEBUG_MODE == 1:
                    print(string)
                else:
                    txt += string + '\n'  #overflow considering after experiment

                    #'''for debugging'''
                    #diff = "i/o each load time is:"+str(time2-time1)
                    #time_avg += (time2-time1)
                    #n += 1
                    #print(diff)
        except DeviceRangeError as e:
            print(e)
            return
        except (KeyboardInterrupt,EOFError):
            #print("avg"+str(time_avg/n))
            if DEBUG_MODE == 0:
                path = './test.txt'
                with open(path,'w') as fd:
                    fd.write('%s %s \n' % (args.timestamp, args.name))
                    fd.write(txt)
            sys.exit(1)


if __name__ == "__main__":
    host = 'localhost' #for socket
    port = 4000
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        while(True):
            s.bind((host,port))
            s.listen(1)
            conn, addr = s.accept()
            msg = conn.recv(1024)
            time_recv = time.time()
            conn.sendall(msg)


    sensing() 
    # gonna give parameter of timestamp following 2 second start


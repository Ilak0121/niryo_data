import os.path
import re
import sys
import time
import argparse

from ina219 import (INA219, DeviceRangeError)

SHUNT_OHMS = 0.1

DEBUG_MODE = 0 #save file or print monitor

def sensing(args):
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
            return
            print(e)
        except (KeyboardInterrupt,EOFError):
            #print("avg"+str(time_avg/n))
            if DEBUG_MODE == 0:
                path = './test.txt'
                fd = open(path,'w')
                fd.write('%s %s \n' % (args.timestamp, args.name))
                fd.write(txt)
                fd.close()
            sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Processing Sensing data with timestamp reservation and testcase naem saving')

    #parser.add_argument('-s', '--save', help='-s [True/False]; save or not', type=bool, default=False)
    parser.add_argument('-n', '--name', help='-n [TESTCASE_NAME]', required=True) 
    parser.add_argument('-t', '--timestamp', type=int, required=True, help= '-t [TIMESTAMP]')

    args = parser.parse_args()
    print(args)

    sensing(args) # gonna give parameter of timestamp following 2 second start


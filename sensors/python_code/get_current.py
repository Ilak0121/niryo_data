import os
import re
import sys
import argparse
import time
from ina219 import (INA219, DeviceRangeError)

SHUNT_OHMS = 0.1

DEBUG_MODE = 0

def sensing(save):
    ina = INA219(SHUNT_OHMS) #need to accurate
    ina.configure()

    p = re.compile('0$')

    #print("shunt_voltage:%.3f mA"%ina.shunt_voltage())
    #print("bus voltage:%.3f mA"%ina.voltage())

    time_avg=0
    n=0
    while(True): #sensing process
        try:
            string = '%.3f'%time.time()
            if not re.search(r'0$', string) == None:
                string += ","
                #time1 = time.time()
                string += '%.4f'%ina.current()
                #time2 = time.time()
                if save == False:
                    print(string)
                    #diff = "i/o each load time is:"+str(time2-time1)
                    #time_avg += (time2-time1)
                    #n += 1
                    #print(diff)
        except DeviceRangeError as e:
            return
            print(e)
        except (KeyboardInterrupt,EOFError):
            #print("avg"+str(time_avg/n))
            sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Processing Sensing data with timestamp reservation and testcase naem saving')

    parser.add_argument('-s', '--save', help='-s [True/False]; save or not', type=bool, default=False)
    parser.add_argument('-n', '--name', help='-n [TESTCASE_NAME]', required=True) 
    parser.add_argument('-t', '--timestamp', type=int, required=True, help= '-t [TIMESTAMP]')

    args = parser.parse_args()
    print(args)

    sensing(args.save)


#https://gongnorina.tistory.com/77
import os.path
import re
import sys
import time
import socket
import json

import smbus
import math

from sensingfinished import SensingFinished
 
# Register
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

bus=0
address=0

DEBUG_MODE = 1 #not debugging
 
def read_byte(reg):
    return bus.read_byte_data(address, reg)
 
def read_word(reg):
    h = bus.read_byte_data(address, reg)
    l = bus.read_byte_data(address, reg+1)
    value = (h << 8) + l
    return value
 
def read_word_2c(reg):
    val = read_word(reg)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val
 
def dist(a,b):
    return math.sqrt((a*a)+(b*b))
 
def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)
 
def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)
 
def sensing():
    global bus
    bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
    address = 0x68       # via i2cdetect
    bus.write_byte_data(address, power_mgmt_1, 0)  #waking up

    #received data extraction
    #(file_path, start_time, end_time, experiment_type) = chunk 

    p = re.compile('0$') #10ms is the period
    save_txt = ''

    start_time = str(float('%.3f'%time.time())+1)
    end_time = str(float('%.3f'%time.time())+3)
    #### first loop for synchronization with each nodes
    while(True): 
        current_time = '%.3f'%time.time()
        if current_time == start_time:
            break


    ###sensing starts
    while(True):
        try:
            end_confirm = string = '%.3f'%time.time()

            if not re.search(r'0$',string) == None:
                # time testing needed and have to adjust
                gyro_xout = read_word_2c(0x43)
                gyro_yout = read_word_2c(0x45)
                gyro_zout = read_word_2c(0x47)
                gyro_xout_scaled = gyro_xout / 131
                gyro_yout_scaled = gyro_yout / 131
                gyro_zout_scaled = gyro_zout / 131
             
                accel_xout = read_word_2c(0x3b)
                accel_yout = read_word_2c(0x3d)
                accel_zout = read_word_2c(0x3f)
                accel_xout_scaled = accel_xout / 16384.0
                accel_yout_scaled = accel_yout / 16384.0
                accel_zout_scaled = accel_zout / 16384.0

                X_Rotation = get_x_rotation(accel_xout_scaled,accel_yout_scaled,accel_zout_scaled)
                Y_Rotation = get_y_rotation(accel_xout_scaled,accel_yout_scaled,accel_zout_scaled)

                string += ','+str('%.5f'%gyro_xout)+','+str('%.5f'%gyro_yout)+','+str('%.5f'%gyro_zout)+','+str('%.5f'%accel_xout)+','+str('%.5f'%accel_yout)+','+str('%.5f'%accel_zout)

                if DEBUG_MODE == 1:
                    print(string)
                else:
                    save_txt += string+'\n'
            ### overflow test needed after experiment
                if end_confirm == end_time:
                    raise SensingFinished

        except (KeyboardInterrupt,EOFError):
            if DEBUG_MODE == 0:
                with open(file_path,'w') as fd:
                    fd.write(save_txt)
            break

        except SensingFinished:  #exception should be making
            if DEBUG_MODE == 0:
                #path = file_path #'./test.txt'
                with open(file_path,'w') as fd:
                    #fd.write('%s %s \n' % (args.timestamp, args.name)) #meta-data for files
                    fd.write(save_txt) #sensor data
            break


if __name__ == "__main__":
    
    # node's ip address (raspi)
    node1 = '192.168.1.207' 
    node2 = '192.168.1.220' 
    node3 = '192.168.1.54' 

    host = node3
    port = 4000

    try:

        print("[STATUS] : Node3 program starting...")
        sensing()



    except (KeyboardInterrupt, EOFError) as e: #ctrl-c let program terminating
        print("[STATUS] : Node3 program finishing...")
        sys.exit(1)

    except Exception as e:
        print(e)
        sys.exit(1)


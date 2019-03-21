#https://gongnorina.tistory.com/77
import os.path
import re
import sys
import time
import argparse
import smbus
import math
 
# Register
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

bus=0
address=0

DEBUG_MODE = 0 #not debugging
 
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
 
def sensing(args):
    bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
    address = 0x68       # via i2cdetect
    bus.write_byte_data(address, power_mgmt_1, 0)  #waking up

    p = re.compile('0$')
    txt = ''
 
    while(True):
        try:
            string = '%.3f'%time.time()
            if not re.search(r'0$',string) == None:
                string += ','
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
                    txt += string+'\n'
        except DeviceRangeError as e:
            print(e)
            return 
        except (KeyboardInterrupt,EOFError):
            if DEBUG_MODE == 0:
                path = './test.txt'
                with open(path,'w') as fd:
                    fd.write('%s %s \n' % (args.timestamp, args.name))
                    fd.write(txt)
            sys.exit(1)


if __name__ == "__main__":

    #parser init
    parser = argparse.ArgumentParser(description='Process IMU sensing with mpu6500') 

    #add parser
    parser.add_argument('-n', '--name', help='-n [TESTCASE_NAME]', required=True) 
    parser.add_argument('-ts', '--timestamp_start', type=int, required=True, help= '-ts [TIMESTAMP_START]')
    parser.add_argument('-te', '--timestamp_end', type=int, required=True, help= '-ts [TIMESTAMP_END]')

    args = parser.parse_args()
    print(args)

    sensing(args)

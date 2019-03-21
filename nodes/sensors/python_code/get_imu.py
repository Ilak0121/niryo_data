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
 
    gryo_xout = read_word_2c(0x43)
    gryo_yout = read_word_2c(0x45)
    gryo_zout = read_word_2c(0x47)
 
    accel_xout = read_word_2c(0x3b)
    accel_yout = read_word_2c(0x3d)
    accel_zout = read_word_2c(0x3f)
 
    accel_xout_scaled = accel_xout / 16384.0
    accel_yout_scaled = accel_yout / 16384.0
    accel_zout_scaled = accel_zout / 16384.0

    print("----------------------------------------------------")
    print("gyro_xout: ", ("%5d" % gryo_xout), " scaled: ", (gryo_xout / 131))
    print("gyro_yout: ", ("%5d" % gryo_yout), " scaled: ", (gryo_yout / 131))
    print("gyro_zout: ", ("%5d" % gryo_zout), " scaled: ", (gryo_zout / 131))
 
    print("---------------------")
    print("accelerometer data")
    print("---------------------")
    print("accel_xout: ", ("%6d" % accel_xout), " scaled: ", accel_xout_scaled)
    print("accel_yout: ", ("%6d" % accel_yout), " scaled: ", accel_yout_scaled)
    print("accel_zout: ", ("%6d" % accel_zout), " scaled: ", accel_zout_scaled)
 
    print("X Rotation: " , get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))
    print("Y Rotation: " , get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))
    print("----------------------------------------------------")

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
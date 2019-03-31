# this script is performed on python2 ( Niryo One )
from niryo_one_python_api.niryo_one_api import *
import rospy

import os.path
import re
import sys
import time
import socket
import json

rospy.init_node('niryo_one_example_python_api')
n=NiryoOne()

conn = None

def case1():
    #-----------------start motions-----------------#
    #n.move_joints([0,0,-1.39,0,0,0]) calibrate_point
    n.calibrate_manual()
    n.move_joints([0,0,0,0,0,0])
    #time.sleep(0.3)
    #n.move_joints([1,-1,-0.6,0,0,0])
    time.sleep(0.3)
    n.move_joints([0,0,0,0,0,0])
    time.sleep(0.3)
    n.move_joints([-1,-1.05,-0.6,0,0,0])
    time.sleep(0.3)
    '''
    #n.move_joints([0,0,0,0,0,0])
    #time.sleep(0.3)
    n.move_joints([1,0.2,0.55,0,0,0])
    time.sleep(0.3)
    n.move_joints([0,0,0,0,0,0])
    time.sleep(0.3)
    n.move_joints([-1,0.2,0.55,0,0,0])
    #n.activate_learning_mode(True)
    '''
    #-----------------finishing motions-------------#
if __name__=="__main__":
    print("[STATUS] : Niryo Time getting Script Mode Start")
    try:
        start_time = time.time()
        case1()
        end_time = time.time()
        print("[INFO] : case's performing time is <"+'%.3f'%(end_time-start_time)+">")
        print("[STATUS] : Niryo Time getting Script Mode Finishing...")
    except NiryoOneException as e:
        print e

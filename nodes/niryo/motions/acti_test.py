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
    n.calibrate_manual()
    #n.move_pose(0,0,0,0,0,0)
    n.move_joints([0,0,0,0,0,0])
    
    time.sleep(1)
    n.move_joints([1.1,-1,-0.6,0,0,0])

    n.activate_learning_mode(True)


if __name__=="__main__":

    node1 = '192.168.1.207' 
    node2 = '192.168.1.220' 
    node3 = '192.168.1.54' 
    node4 = '192.168.1.187' 

    host = node4
    port = 4000

    print("[STATUS] : Niryo Robot Script Mode Start")

    try:
        #test()
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(None)
        s.bind((host,port))
        s.listen(1)
        
        while(True):
            conn, addr = s.accept()
            conn.sendall("[STATUS] : Node4 socket connection established...".encode())
            conn.sendall("[STATUS] : Node4 program finishing completely....".encode())

            start = time.time()
            case1()
            end = time.time()

            conn.sendall("[INFO] : Duration Time : {}...".format(str(end-start)).encode())
            time.sleep(0.5)

            conn.sendall("[STATUS] : Sensing finished...".encode()) #key data to finish

    except NiryoOneException as e:
        if not conn == None:
            conn.sendall("[ERROR] : Node4 program NiryoOneException occur!!".encode())
            conn.sendall("[ERROR] : Node4 program terminating....".encode())
            conn.sendall(str(e).encode())
        else: 
            print("[Error] : Niryo Robot NiryoOneException occured!")
            print("[Error] : Error message is : {"+str(e)+"}")
        s.close()
        sys.exit(1)

    except Exception as e:
        if not conn == None:
            conn.sendall("[ERROR] : Node4 program unexpected exception event occur!!".encode())
            conn.sendall("[ERROR] : Node4 program terminating....".encode())
            conn.sendall(str(e).encode())
        else: 
            print("[DEBUG] : Node4 program terminating...")
            print("[DEBUG] : Error message is : {"+str(e)+"}")
        s.close()
        sys.exit(1)

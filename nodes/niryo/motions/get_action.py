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

def case(chunk,conn):

    (file_path, start_time, end_time, experiment_type) = chunk 
    start_time='%.3f' % (float(start_time)+0.5) #trouble shooting ; python2 str(float) goes to '.2f'
    ## start time same?
    ## end time -2? compare to sensors?

    ###p = re.compile('0$') #10ms period / not need here, niryo

    #conn.sendall("[STATUS] : Niryo start time waitting...".encode())

    while(True): 
        current_time = '%.3f'%time.time()
        if current_time == start_time:
            break

    conn.sendall(("[STATUS] : Niryo motion starts as type of "+experiment_type+"....").encode())

    #-----------------start motions-----------------#
    '''
    n.calibrate_manual()
    n.move_joints([0,0,0,0,0,0])
    time.sleep(0.3)
    n.move_joints([0,-0.86,-0.6,0,0,0])
    time.sleep(0.3)
    n.activate_learning_mode(True)
    '''
    n.calibrate_manual()
    n.move_joints([0,0,-1.39,0,0,0]) #calibrate_point
    time.sleep(0.3)
    n.move_joints([-0.667,-0.503,-0.159,0.2,0.01,0])
    time.sleep(0.3)
    n.move_joints([0,0,-1.39,0,0,0]) #calibrate_point
    n.activate_learning_mode(True)
    #-----------------finishing motions-------------#

    real_end_time = float("%.3f"%time.time())
    print(("[INFO] : real_end_time:" + '%.3f'%real_end_time + ', end_time : '+end_time).encode())
    if float(end_time) < real_end_time:
        conn.sendall("[WARN] : Node4 finished eariler than sensing finished...".encode())
        raise Exception
    else:
        conn.sendall("[STATUS] : Node4(niryo) motion script finished completely..".encode())

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
           
            data = conn.recv(1024)
            data = json.loads(data.decode())

            #start = time.time()
            case(data.get('attr'),conn)# case motion
            #end = time.time()
            #conn.sendall("[INFO] : Duration Time : {}...".format(str(end-start)).encode())
            #conn.sendall("[INFO] : timestamp is "+str(time.time()))

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

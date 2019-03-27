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


def test():
    n.calibrate_manual()
    #n.move_pose(0,0,0,0,0,0)
    n.move_joints([0,0,0,0,0,0])
    
    time.sleep(1)
    n.move_joints([1.1,-1,-0.6,0,0,0])


if __name__=="__main__":

    node1 = '192.168.1.207' 
    node2 = '192.168.1.220' 
    node3 = '192.168.1.54' 
    node4 = '192.168.1.187' 

    host = node4
    port = 4000

    print "[STATUS] : Niryo Robot Script Mode Start"


    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        try:
            try:
                s.bind((host,port))
                s.listen(1)
            except Exception as e:
                print("[DEBUG] : Bind & Listening error, port number confirm or wait for socket arrange")
                sys.exit(1)

            print("[STATUS] : Niryo Server program starting...")

            while(True):
                conn, addr = s.accept()
                conn.sendall("[STATUS] : Niryo socket connection established...".encode())

                data = conn.recv(1024)
                data = json.loads(data.decode())

                #sensing(data.get('attr'),conn) #processing
                #test()

                conn.sendall("[STATUS] : Sensing finished...".encode()) #key data to finish to sening controller. (protocol) dont touch

        except (KeyboardInterrupt, EOFError) as e: #ctrl-c let program terminating
            print "[DEBUG] : Ctrl-C pressed!!"
            print "[DEBUG] : Niryo Script process Terminating.."
            sys.exit(1)

        except NiryoOneException as e:
            print "[DEBUG] : Niryo Robot Exception occured!!"
            print e

        except Exception as e:
            conn.sendall("[ERROR] : Niryo Server program unexpected exception event occur!!".encode())
            conn.sendall("[ERROR] : Niryo Server terminating....".encode())
            print(e)
            sys.exit(1)


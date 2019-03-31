from niryo_one_python_api.niryo_one_api import *
import rospy
import time

rospy.init_node('niryo_one_example_python_api')

print("---start")

n=NiryoOne()

try:
    #move_pose(0,0,0,0,0,0)
    n.calibrate_manual()
    #n.move_joints([0,0,0,0,0,0])
    
    #time.sleep(1)
    #n.move_joints([1.1,-1,-0.6,0,0,0])
    n.activate_learning_mode(True)
    '''
    time.sleep(1)
    n.move_joints([1.1,0,0,0,0,0])
    
    time.sleep(1)
    n.move_joints([-1.1,0,0,0,0,0])
    
    time.sleep(1)
    n.move_joints([-1.1,-1,-0.6,0,0,0])

    time.sleep(1)
    n.move_joints([0,0,0,0,0,0])

    time.sleep(1)
    n.move_joints([0,0,-1.3,0,0,0])
    '''
    
    '''
    while a<5:
        n.move_joints([0.53, 0.22, -0.29, 0, 0.21, 0.02])
        time.sleep(0.5)
        n.move_joints([0, -0.13, -0, 0.1, 0.11, 0.02])
        time.sleep(0.5)
        n.move_joints([-0.53, 0.22, 0.29, 0, 0.21, 0.02])
        a=a+1
    '''
    #n.calibrate_auto()
    print("finishing")

except NiryoOneException as e:
    print(e)

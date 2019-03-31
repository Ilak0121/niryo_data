from niryo_one_python_api.niryo_one_api import *
import rospy
import time

rospy.init_node('niryo_one_example_python_api')

print "---start"

n=NiryoOne()

try:
    while True:
        n.move_joints([0,-0.2,-1.327,0,0,0])
        time.sleep(1)
        n.move_joints([0,0.2,-1.327,0,0,0])
        time.sleep(1)

    print "finishing"

except NiryoOneException as e:
    print e
print "--end"

from niryo_one_python_api.niryo_one_api import *
import rospy
import time
import sys

rospy.init_node('niryo_one_example_python_api')

print "[STATUS] : Niryo Robot Learning Mode Start"

n=NiryoOne()

try:
    n.calibrate_manual()
    
    n.activate_learning_mode(True)

except NiryoOneException as e:
    print "[DEBUG] : Niryo Robot Exception occured!!"
    print e

print "[STATUS] : Niryo Robot Learning Mode Finished."

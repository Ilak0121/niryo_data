#!/usr/bin/env python

# To use the API, copy these 4 lines on each Python file you create
from niryo_one_python_api.niryo_one_api import *
import rospy
import time

rospy.init_node('niryo_one_example_python_api')

print "--- Start"

n = NiryoOne()

try:
    # Calibrate robot first
    n.calibrate_manual()
    print "Calibration finished !"

    # Test learning mode
    n.activate_learning_mode(False)

    #n.activate_learning_mode(True)

except NiryoOneException as e:
    print e 
    # handle exception here
    # you can also make a try/except for each command separately

print "--- End"







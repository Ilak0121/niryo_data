from niryo_one_python_api.niryo_one_api import *
import rospy
import time
import sys
from niryo_one_msgs.msg import HardwareStatus

rospy.init_node('niryo_one_example_python_api')

print("---start")

f=open('./temper/test.txt','a')

try:
    while True :
        line=''
        hw_status = rospy.wait_for_message('niryo_one/hardware_status',HardwareStatus,timeout=5)
        temp_status=hw_status.temperatures
        print(temp_status)
        for i in range(0,6):
            line = line+str(temp_status[i])+" "
        #print(line)
        f.write(line+'\n')
        time.sleep(0.01)

except NiryoOneException as e:
    print(e)
except:
    f.close()
    exit()

print("--end")

from niryo_one_python_api.niryo_one_api import *
import rospy
import time
import sys
from niryo_one_msgs.msg import HardwareStatus

rospy.init_node('niryo_one_example_python_api')


print("---test start---")

f=open('./temper/test.txt','a')

try:
    while True :
        timestamp1=time.time()
        temp_status = rospy.wait_for_message('niryo_one/hardware_status',HardwareStatus,timeout=5).temperatures
        timestamp2=time.time()
        #line=str(timestamp)+" "
        #line = line+str(temp_status[0])+" "
        #temp_status[1]+" "
        #temp_status[2]+" "
        #temp_status[3]+" "
        #temp_status[4]+" "
        print timestamp2-timestamp1
        #f.write(line+'\n')
        #time.sleep(1)

except NiryoOneException as e:
    print(e)
except:
    f.close()
    exit()

print("--end")

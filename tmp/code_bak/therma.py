import spidev
import time
import os

#open spi bus

# Function to read spi data from mcp3008 chip
# channel must be an interger 0-7
def ReadChannel(channel):
    adc1 = spi.xfer([0x3b])
    time.sleep(0.1)
    adc2 = spi.xfer([0x3d])
    time.sleep(0.1)
    adc3 = spi.xfer([0x3f])
    time.sleep(0.1)

    print(adc1)
    print(adc2)
    print(adc3)
    #data = ((adc[1]&3)<<8)+adc[2]
   # data=adc
    #return data

spi= spidev.SpiDev()
spi.open(0,0) # bus,device
spi.max_speed_hz=1000000

temp_channel =0
delay = 2 
spi.writebytes([0x6b])
#spi.xfer([0x00])

'''
while True:
    print("-----------------------------")
    for i in range(0,5):
        ReadChannel(i)
    time.sleep(delay)
'''


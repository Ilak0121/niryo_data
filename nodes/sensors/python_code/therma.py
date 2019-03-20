import spidev
import time
import os

#open spi bus
spi= spidev.SpiDev()
spi.open(0,0) # bus,device
spi.max_speed_hz=1000000

# Function to read spi data from mcp3008 chip
# channel must be an interger 0-7
def ReadChannel(channel):
    adc = spi.xfer2([1,channel,0])
    print(adc)
    #data = ((adc[1]&3)<<8)+adc[2]
    data=adc
    return data

temp_channel =0
delay = 2 

while True:
    print("-----------------------------")
    for i in range(0,5):
        temp_level = ReadChannel(i)
    time.sleep(delay)




import wiringpi as wp
import time

wp.wiringPiSetup()
wp.wiringPiSPISetup(0,500000)

mgmt1=0x6b
mgmt2=0x6c

buf = bytes([mgmt1,0x80,0x00])
retlen,retdata = wp.wiringPiSPIDataRW(0,buf)
time.sleep(5)

print(retlen)
print(retdata)
print()
print()
buf = bytes([mgmt2,0x00,0x00])
retlen,retdata = wp.wiringPiSPIDataRW(0,buf)
time.sleep(5)

print(retlen)
print(retdata)
print()
print()

buf = bytes([0x43,0x00,0x00])
retlen,retdata = wp.wiringPiSPIDataRW(0,buf)
time.sleep(5)

print(retlen)
print(retdata)


print()
print()

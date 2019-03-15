from ina219 import INA219
from ina219 import DeviceRangeError

SHUNT_OHMS = 0.1

def read():
    ina = INA219(SHUNT_OHMS)
    ina.configure()

    try:
        #print("bus current:%.3f mA"%ina.shunt_voltage())
        print("bus current:%.3f mA"%ina.voltage())
        #print("bus current:%.3f mA"%ina.current())
    except DeviceRangeError as e:
        print(e)

if __name__ == "__main__":
    while(True):
        read()

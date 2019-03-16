#include <iostream>
#include "ina219.h"
#include <wiringPiI2C.h>
#include<unistd.h>
//#include <reading.h>
using namespace std;

int main(){
    INA219 ina219 = INA219(0x40);
    ina219.configure(CONF_32V_2A);

    while(1){
        double shuntVolts  = wiringPiI2CReadReg16(ina219.m_fd, INA219_REG_SHUNTVOLTAGE) * 0.01;
        double busVolts  = wiringPiI2CReadReg16(ina219.m_fd, INA219_REG_BUSVOLTAGE) * 0.001;
        double volts = busVolts + (shuntVolts / 1000);

        wiringPiI2CWriteReg16(ina219.m_fd, INA219_REG_CALIBRATION, ina219.m_calValue);
        double current  = wiringPiI2CReadReg16(ina219.m_fd, INA219_REG_CURRENT) / ina219.m_currentDivider;
        cout<<shuntVolts<<endl;

        sleep(1);

    }
    return 0;
}

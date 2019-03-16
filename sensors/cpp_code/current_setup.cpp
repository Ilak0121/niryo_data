#include<iostream>
#include<errno.h>
#include<math.h>
#include<wiringPiI2C.h>
using namespace std;

extern uint16_t cal, config;
extern float r_shunt,current_lsb,power_lsb;

void configure(int fd){
    config = 0;
    //config |= (range<<BRNG | gain<<PG0 | bus_adc << BADC1 | shunt_adc <<SADC1|mode);
    //config |= (RANGE_32V<<BRNG | GAIN_8_320MV<<PG0 | ADC_12BIT << BADC1 | ADC_12BIT << SADC1 | CONT_SH_BUS);
    config |= (1<<13 | 3<<11 | 3<<7 | 3 << 3 | 7);
    int result = wiringPiI2CWriteReg16(fd, 0x00,config);
    if(result == -1)
        cout<<"Error, is :"<<errno<<endl;
}

void calibrate(int fd,float shunt_val, float v_shunt_max, float v_bux_max, float i_max_expected){
    uint16_t digits;
    float min_lsb,swap;

#if (INA219_DEBUG ==1)
    float max_current,max_before_overflow,max_shunt_v,max_shunt_v_before_overflow, max_power, i_max_possible,max_lsb;
#endif

    r_shunt = shunt_val; 
    min_lsb = i_max_expected / 32767;

    current_lsb = min_lsb; 
    digits = 0;

    while(current_lsb > 0.0){
        if((uint16_t)current_lsb /1){
            current_lsb = (uint16_t) current_lsb +1;
            current_lsb /= pow(10,digits);
            break;
        }else{
            digits++;
            current_lsb *= 10.0;
        }
    };

    swap = (0.04096)/(current_lsb*r_shunt);
    cal = (uint16_t)swap;
    power_lsb = current_lsb *20;
    int result = wiringPiI2CWriteReg16(fd, 0x05,cal);
    if(result == -1)
        cout<<"Error, is:"<<errno<<endl;

}

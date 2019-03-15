#include<stdio.h>
#include<iostream>
#include<errno.h>
#include<wiringPiI2C.h>
#include<sys/time.h>
#include<unistd.h>
#include<math.h>
using namespace std;

uint16_t cal, config;
float r_shunt,current_lsb,power_lsb;

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
            current_lsb /= pow(10,digits); //pow need to check
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

void configure(int fd){
    config = 0;
    //config |= (range<<BRNG | gain<<PG0 | bus_adc << BADC1 | shunt_adc <<SADC1|mode);
    //config |= (RANGE_32V<<BRNG | GAIN_8_320MV<<PG0 | ADC_12BIT << BADC1 | ADC_12BIT << SADC1 | CONT_SH_BUS);
    config |= (1<<13 | 3<<11 | 3<<7 | 3 << 3 | 7);
    int result = wiringPiI2CWriteReg16(fd, 0x00,config);
    if(result == -1)
        cout<<"Error, is :"<<errno<<endl;
}




int main(){
    int fd,result;
    long long milliseconds;
    struct timeval te;

    unsigned char buffer[100];

    fd = wiringPiI2CSetup(0x40); //address
    cout<<"Init result:"<<fd<<endl;

    configure(fd);
    //calibrate(fd, D_SHUNT, D_V_SHUNT_MAX, D_V_BUS_MAX, D_I_MAX_EXPECTED);
    calibrate(fd, 0.1 , 0.2 , 32, 2);


    for(int i=0;i<0x0000ffff;i++){

        //result = wiringPiI2CWriteReg16(fd,0x40,(i&0xfff));
        //result = wiringPiI2CWriteReg8(fd,0x40,(i&0xfff));
        //result = wiringPiI2CReadReg16(fd,0x40,(i&0xfff));
        //result = wiringPiI2CReadReg8(fd,0x40,(i&0xfff));
        
        if(result == -1)
            cout<<"Error. Error is:"<<errno<<endl;
    }

    return 0;
}

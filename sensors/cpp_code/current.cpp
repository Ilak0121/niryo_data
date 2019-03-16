#include<stdio.h>
#include<iostream>
#include<errno.h>
#include<wiringPiI2C.h>
#include<sys/time.h>
#include<unistd.h>
using namespace std;

uint16_t cal, config;
float r_shunt,current_lsb,power_lsb;


void configure(int fd);
void calibrate(int fd,float shunt_val, float v_shunt_max, float v_bux_max, float i_max_expected);

int main(){
    int fd;
    int16_t result;

    long long milliseconds; //for timestamp
    struct timeval te;

    unsigned char buffer[100];

    fd = wiringPiI2CSetup(0x40); //address
    //cout<<"Init result:"<<fd<<endl;

    configure(fd);
    //calibrate(fd, D_SHUNT, D_V_SHUNT_MAX, D_V_BUS_MAX, D_I_MAX_EXPECTED);
    calibrate(fd, 0.1 , 0.2 , 32, 2);


    while(1){

        //result = wiringPiI2CWriteReg16(fd,0x40,(i&0xfff));
        //result = wiringPiI2CWriteReg8(fd,0x40,(i&0xfff));
        //result = wiringPiI2CReadReg16(fd,0x40,(i&0xfff));
        //result = wiringPiI2CReadReg8(fd,0x40,(i&0xfff));
        result = wiringPiI2CReadReg16(fd, 0x04);//0x02);
        //result *= current_lsb;
        
        if(result == -1)
            cout<<"Error. Error is:"<<errno<<endl;
        else
            cout<<"value:"<<result<<endl;//*current_lsb<<endl;
    }

    return 0;
}

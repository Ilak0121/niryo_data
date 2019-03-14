#include<stdio.h>
#include<iostream>
#include<errno.h>
#include<wiringPiI2C.h>

using namespace std;

int main(){
    int fd,result;

    unsigned char buffer[100];

    fd = wiringPiI2CSetup(0x40); //address

    cout<<"Init result:"<<fd<<endl;

    for(int i=0;i<0x0000ffff;i++){

        result = wiringPiI2CWriteReg16(fd,0x40,(i&0xfff));

        if(result == -1)
            cout<<"Error. Error is:"<<errno<<endl;
    }

    return 0;
}

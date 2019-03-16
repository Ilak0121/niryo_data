#include<stdio.h>

enum testing { a=1,b=2,c=3};

int main(){
    testing merci = b;
    int test = b;
    printf("%d %d \n",merci,test);
    return 0;
}

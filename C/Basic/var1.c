#include <stdio.h>

int globalInt = 100;
char globalChar ='g';

int main() {
    int localInt =10;
    long localLong = 23456789;
    double localDouble = 2.3;
    char localChar = 'A';
    char localString[20] = "Learn";
    int a,b;
    //now lets print the adress of the each vaiable
    printf("globalint adress is %p and value is is %d, %d \n", &globalInt, globalInt, sizeof(int));
    printf("globalchar adress is %p and value is is %c, %d \n", &globalChar, globalChar, sizeof(char));
    printf("====Global Variable Over ====\n ");
    printf("localchar adress is %p and value is is %c, %d \n" ,&localChar, localChar, sizeof(char));
    printf("localdouble adress is %p and value is is %lf, %d \n", &localDouble, localDouble, sizeof(double));
    printf("locallong adress is %p and value is is %lu, %d \n" ,&localLong, localLong, sizeof(char));
    printf("localint adress is %p and value is is %d, %d \n" , &localInt, localInt, sizeof(int));
    printf("localString adress is %p and value is is %s, %d\n", &localString, localString, sizeof(localString));
}
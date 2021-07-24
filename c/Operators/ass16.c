#include<stdio.h>
int main(int args, char*argv[]) {
    float a,b,c,d,e,g;
    a=3.4; b=34.4; c=55.6; d=43.4; e=3.4;
    //printf("Enter the values\n");
    //scanf ("%f %f %f %f %f ", &a, &b, &c, &d, &e);
    g=(a+b+c+d+e)/5;
    printf("Average value is %f", g);
    return 1;

}
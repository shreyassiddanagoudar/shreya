#include<stdio.h>
 int main (int argc, char*args[]){
     int a,b;
     a=3; b=4;

     printf ("Value of integer a= %d \n",a,b);
     printf ("Value of integer a=%d \n", a<<1);
     printf ("Value of integer a=%d \n", a<<b);
     printf ("Value of integer a=%d \n", a>>b);
     printf ("Value of integer a=%d \n", a&b);
     printf ("Value of integer a=%d \n", ~a);
     printf ("Value of integer a=%d \n", a||b);


 }
#include <stdio.h>

int main(int argc, char*argv[]) {

int a,b;
printf("Enter the number \n");
scanf ("%d", &a);
if ( a%4 ==0 && a%100 !=0) 
{
printf("The given year is a leap year \n");
}
else 
{
printf("The given year is not a leap year \n");
}
}
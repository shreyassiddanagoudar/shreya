#include <stdio.h>

int main(int argc, char*argv[]) {

int clh,cla, att;
printf("Enter the number of classes held \n");
scanf ("%d", &clh);
printf("Enter the number classes attended \n");
scanf ("%d", &att);
cla = att*0.75;
if( cla > clh) 
{
printf("The student is elligible\n");
}
else 
{
printf ("The student is not elligible");
}
}
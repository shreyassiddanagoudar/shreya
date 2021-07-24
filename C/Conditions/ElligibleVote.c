#include <stdio.h>

int main(int argc, char*argv[]) {

int a,cla, att;
printf("Enter the age of the candidate \n");
scanf ("%d", &a);

if( a >= 18) 
{
printf("The candidate is elligible to cast a vote\n");
}
else 
{
printf ("The candidate is not elligible to cast a vote");
}
}
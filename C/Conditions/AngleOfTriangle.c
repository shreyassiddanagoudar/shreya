#include <stdio.h>

int main(int argc, char*argv[]) {

int a,b,c, sum;
printf("Enter the angle for a triangle \n");
scanf ("%d %d %d", &a, &b, &c);
sum = a+b+c;
if(sum=180) 
{
  printf("The triangle can be formed \n");
}
else 
{
  printf ("The triangle cannot be formed");
}
}
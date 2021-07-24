#include <stdio.h>
int main (int argc, char*argv[]) {
int n;
printf("Enter the number\n");
scanf("%d", &n);

int temp =n;
int numOfDigit = 0;
int maxmul = 0;
 while (n>0) {
     n= n/10;
     numOfDigit = numOfDigit+1;
if(maxmul ==0) {
    maxmul =1;
}
else
maxmul = maxmul*10;
printf("%d %d\n", numOfDigit, maxmul); 
printf ("%d %d %d %d\n", n, temp, maxmul, numOfDigit);
}
 int digit;
 int res;
 int mul =1;
 
 for (int i=1; i<= numOfDigit; i++) {
     digit = temp%10;
     if (i==1) {
     res = digit * maxmul;
     }
     else if (i==numOfDigit) {
         res =res +digit;
     }
     else {
     res = res +digit*mul;
     }
     mul = mul*10;
     printf("maxmul is %d \n", mul);
     temp = temp/10;
 }
 printf("res is %d \n", res);
 }
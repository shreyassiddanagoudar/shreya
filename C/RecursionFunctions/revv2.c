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

}
 int digit;
 int res=0;
 int mul =1;
 
 for (int i=1; i<= numOfDigit; i++) {
     digit = temp%10;
     res = res + digit*maxmul;
     maxmul = maxmul/10;
     temp=temp/10;
    
 }
 printf("res is %d \n", res);
 }
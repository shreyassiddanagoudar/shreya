#include <stdio.h>
int main (int argc,char*argv[]) {
    int i, n, digit, arms=0,temp, temp1, rem, power, sum;
    printf ("Enter the number:\n");
    scanf("%d", &n);
    temp = n;
    temp1=n;
    while (temp>0) {
     rem = temp%10;
     power = 1;

     for (int i=1; i<=rem; i++) {
         power =power*i;
        }
        arms = arms+power;
     
     printf("%d \n", power);
     printf("%d \n", arms );
     temp /=10;
    }
   
     if (temp1 == arms) {
         printf("the given number %d is strong", temp1);
     }
         else {
             printf(" the given number is not strong", temp1);
             }
}
#include <stdio.h>
int main (int argc,char*argv[]) {
    int i, n, digit, arms=0,temp, temp1, rem, power, sum;
    printf ("Enter the number:");
    scanf("%d %d", &n, &n);
    temp = n;
    temp1 = n;
     while(n>0) {
         n = n/10;
         digit++;
        }
    while (temp>0) {
     rem = temp%10;
     power = 1;

     for (int i=1; i<=digit; i++) {
         power =power*rem;
        }
        arms = arms+power;
     
     printf("%d \n", power);
     printf("%d \n", arms );
     temp /=10;
    }
    
     if (temp1 == arms) {
         printf("the given number %d is armsstrong", temp1, sum);
     }
         else {
             printf(" the given number is not an armsstrong", temp1);
             }
}
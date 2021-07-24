#include<stdio.h>
int main(int argc,char*argv[]) {
    int n;
    int result=0;
    printf("swap the first and last digit of a number");
    printf("enter the number :\n");
    scanf("%d", &n);

    int firstdigit = -1;
    int multiplier =1;
    int digit;
    int cnt =1;
    while(n >10) {
        digit =n % 10;

        if (firstdigit == -1) {
            firstdigit = digit;
        }
        else 
            result = result + (digit * multiplier);
            multiplier = multiplier*10;
            n = ( n / 10);
              
              printf ("loop#: %d first digit: %d digit: %d multiplier: %d num: %d result:%d \n", cnt, firstdigit,  multiplier, n, result);
            cnt++;
    }
    result = result +n;
    printf ("digit: %d multiplier: %d num: %d result:%d \n", cnt, firstdigit, multiplier, n, result);
            cnt++;
            result = result + firstdigit * multiplier;
            printf("after digit swap\n");
            printf("%d",result);

    }

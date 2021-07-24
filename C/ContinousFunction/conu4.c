#include<stdio.h>
int main() {
    int num =1;
    int sum = 0;

    checkcond:
    if(num>100) {
        printf("%d", sum);
        return -1;
    }
    if (num%2 !=0) {
        sum = sum+num;
        printf("%d\n", sum);
    }
    num=num+1;
    goto checkcond;
}

#include<stdio.h>
int main(int args, char*argv[]) {
    int a,b;
    float c;

    printf("Enter the first value: ");
    scanf("%d ",&a);
    printf("Enter the second value: ");
    scanf("%d ",&b);

    c=(a+b)/2;
    printf("Average value is %d and %d is : %.3f", c,a,b);

    return 1;

}
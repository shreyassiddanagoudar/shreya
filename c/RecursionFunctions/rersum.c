#include<stdio.h>

int sumDigit(int n) {

if (n==0) {
    return 0;
}
int d = n%10;
return d + sumDigit(n/10);
}

int main() {
     int num, add;
    printf("Enter the number");
    scanf("%d", &num);
    add = sumDigit(num);
    printf("%d", add);
}
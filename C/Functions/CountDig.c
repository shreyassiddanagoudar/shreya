#include<stdio.h>

int countDigit(int n) {

if (n==0) {
    return 0;
}
return 1 +countDigit(n/10);
}

int main() {
     int num, count;
    printf("Enter the number");
    scanf("%d", &num);
    count = countDigit(num);
    printf("%d", count);
}
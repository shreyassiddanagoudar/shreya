#include<stdio.h>

int prodDigit(int n) {

    if(n == 0) {
        return 1;
    }
    int d = n%10;
    return d * prodDigit(n/10);
}

int main() {
    int n, prod;
    printf("Enter the number:");
    scanf("%d", &n);
    prod = prodDigit(n);
    printf("%d", prod);
}
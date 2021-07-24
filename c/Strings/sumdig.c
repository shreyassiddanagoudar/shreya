#include<stdio.h>

int sum(int n) {
    if(n==0) {
        return 0;
    }
    else {
    int dig = n%10;
    return dig + sum(n/10);
    }
}

int main() {
    int res, n;
    printf("Enter the number ");
    scanf("%d",&n);
    res = sum(n);
    printf("Sum of returned digit is %d:", res);
}
#include<stdio.h>
int ones(int n) {
    if (n < 10) {
        return n == 1;
    }
    int d=n%10;
    return ( d==1 )+ones(n/10);
}
int main() {
int n;
printf("Enter the number \n");
scanf("%d", &n);
// int c = ones(n);
printf("%d", ones(n));
}
   
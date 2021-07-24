#include <stdio.h>

int fib(int n) {
    printf("%d", n);
    if (n == 0) {
        return 0 ;
    }
    if (n == 1) {
        return 1;
    }
    else {
    int fa = fib(n-1 ) + fib(n-2);
    }
}


int main() {
    int n;
    printf("Enter the number");
    scanf("%d", &n);
    int fa = fib(n);
    printf("%d", fa);
}
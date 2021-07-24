#include <stdio.h>

int gcd(int a, int b) {
    if (a%b == 0) {
        return b ;
    }
    else {
        return gcd(b, a%b);
    }
}


int main() {
    int a,b;
    printf("Enter the values for a and b");
    scanf("%d %d", &a, &b);
    int fa = gcd(a,b);
    printf("%d", fa);
}
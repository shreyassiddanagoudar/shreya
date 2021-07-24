#include<stdio.h>
#include<stdlib.h>
#include<memory.h>

int sum(int a, int b, int n) {
    for(int n=1; n<5; n++) {
    printf("%d %d sum of two numbers is %d \n", a*n, b*n, a*n+b*n);
    }
}
int main() {
    double (*fn)(int, int);
    // sum = a+b;
    fn* = &sum;
    fn(5.2,6.3);
    printf("%d", &sum);
    return 0;

}

#include<stdio.h>
#include<stdlib.h>
#include<memory.h>

int sum(int a, int b) {
    printf("%d %d sum of two numbers is %d \n", a, b, a+b);
}
int main() {
    int (*fn)(int, int);
    // sum = a+b;
    fn = &sum;
    fn(5,6);
    printf("%d", fn);
    //return fn;

}

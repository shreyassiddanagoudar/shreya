#include<stdio.h>
#include<stdlib.h>
#include<memory.h>

int max(int *a, int *b) {
        if(*a<*b) {
           return *b;
        }
        return *a;
}

int main() {
    int a=9,b=10;
    int (*fn) (int, int);
    // *fn(max);
    fn = &max;
    int max=fn(&a,&b);
    // fn != &m;
    printf("the max value between two numbers is %d \n", max);
}
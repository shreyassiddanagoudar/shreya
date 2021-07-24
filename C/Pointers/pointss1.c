#include<stdio.h>
#include<stdlib.h>

int main(int argc, char*argv[]) {
    int *pc;
    int *pm;
    int a;
    int b;
    int c;
    pc=&a;
    pm=&b;
    printf("%p of pc-%p %p %p of pm is \n ", &pc,pc,&pm,pm);
    // printf("%p", *a,*b);
    *pc=10;
    printf("%p %p %d\n", &pc,pc,&pc);
    *pm=20;
     a=*pc + *pm;
     
}
#include<stdio.h>
#include<stdlib.h>

int main(int argc, char*argv[]) {
    int *pm;
    int *pc;
    int a;
    int b;
    pm=&a;
    pc=&b;
    int *p;
    // printf("%p %p %p %p", &pm, pm, &pc, pc);
    *pm=6;
    printf("%p %p %p \n", &pm, pm, &pm);
    *pc=5;
    printf("%p %p %p \n", &pc, pc);
    *p=*pm + *pc;
    printf("%p %p %p \n",*p);
    return *p;   
}


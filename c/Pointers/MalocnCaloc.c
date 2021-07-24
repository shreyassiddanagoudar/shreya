#include<stdio.h>
#include<stdlib.h>

int main (int argc, char*argv[]) {
    int *pc;
    int*pn;
    int a;

    pc=(int *)calloc(1, sizeof(int));
    pm =(int *)malloc(sizeof (int);

    *pc = 10;
    *pn = 20;
    a = *pc +*pn;
    printf("adress of pc:%p and value of pc: %p and its content is %d \n", &pc, pc, *pc);
    printf("adress of pc:%p and value of pc: %p and its content is %d \n", &pn, pn, *pn);
    printf("adress of pc:%p and value of a: %d \n", &a, a);
    }

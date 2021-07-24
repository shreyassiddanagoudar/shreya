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

printf("adress of &pc is-%p adress of pc is-%p adress of &pm is-%p adress of pm is-%p \n ", &pc, pc, &pm, pm);
*pc=20;
printf("adress %p value %d adress %p\n", &pc, pc, &pc);
*pm=30;
printf("adress %p value %d adress %p \n", &pm, pm, &pm);
c=*pc+*pm;
}
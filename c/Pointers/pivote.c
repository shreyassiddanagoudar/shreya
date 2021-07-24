#include<stdio.h>

int main() {
int a=5;
int *p;
p= &a;
printf("adress of main:%p \n", main);
printf("adressof a: %p \n",&p);
printf("adress of p:%p \n", &p);
printf("adress of p: %p\n",p);
// printf("adress of p: %p\n",p);
printf("adress os a:%d\n",a);
printf("value of content pointed by p:%d\n", *p);
}
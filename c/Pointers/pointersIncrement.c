#include<stdio.h>

int main() {
  int *p1;
  char*p2;
  double *p3;

  int a=8;

  printf("adress of a: %x and value of a:%d \n", &a, a);
  printf("adress of p1: %x and value of p1:%x and points to %d\n", &p1, p1, &p1);
  printf("adress of p2: %x and value of p2:%x \n", &p2, p2);

  a++;
  p1++;
  p2++;
  p3++;
 printf("adress of a: %x and value of a:%d \n", &a, a);
 printf("adress of p1: %x and value of p1:%x and points to %d\n", &p1, p1, &p1);
 printf("adress of p2: %x and value of p2:%x and points to %d\n", &p2, p2, &p2);
 printf("adress of p3: %x and value of p3:%x and points to %d\n", &p3, p3, &p3);
return 1;
}
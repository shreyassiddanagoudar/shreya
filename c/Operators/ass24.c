#include<stdio.h>

int main(int argc, char*argv[]) {
      char a,b;
    printf ("Enter the name: \n", a);
    scanf("%c",&a);
    printf ("Enter the age: \n",b);
    scanf("%c",&b);

printf("the name and age is %c", &a, &b);
return 1;
    
}
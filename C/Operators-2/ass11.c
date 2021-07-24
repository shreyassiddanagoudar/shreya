#include <stdio.h>
 int main(int argc, char*argv[]) {
    
    int a;
    printf ("Enter the value for a:\n");
    scanf("%d", &a);
    printf("value of is %d \n", ++a);
    printf ("value of is %d \n", a--);
    printf ("value of is %d \n", --a);
    printf ("value of is %d \n", a++);

    return 1;

 }
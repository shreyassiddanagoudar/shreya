#include <stdio.h>
int main(int args, char*argv[]) {
    
    int a,b,c;
    printf ("Please enter the value for a=\n");
    scanf("%d", &a);
    printf ("Please enter the value for b=\n");
    scanf("%d", &b);
    c=a+b;
    printf("c= %d \n", c);
    c=a-b;
    printf ("c= %d \n", c);
    c=a/b;
    printf ("c= %d \n", c);
    c=a*b;
    printf ("c= %d \n", c);
    c=a%b;
    printf ("c= %d \n", c);

}

#include <stdio.h>

int main(int argc,char*argv[]) {
    int a, b, c;
    printf("Enter the age: \n");
    scanf("%d %d %d",  &a, &b, &c);

    if (a>b && a>c)
    {
        printf("a is the oldest \n ", a);
    }
    else if (b>a && b>c)
    {
         printf("b is the oldest \n ", b);
    }
    else if(c>a && c>b)
    {
         printf("c is the oldest \n ", c);
    }
    else if(a<b && a<c)
    {
         printf("a is the youngest \n ", a);
    }
    else if(b<a && b<c)
    {
         printf("b is the youngest \n ",b );
    }
    else if(c<a && c<b)
    {
         printf("c is the youngest \n ",c );
    } 
   
}
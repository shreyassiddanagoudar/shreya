#include <stdio.h>

int main(int argc,char*argv[]) {
    int m,n;
    printf("Enter the integer: \n");
    scanf("%d",  &m);

    if (m>0)
    {
        printf("value of n is 1 \n ", m);
    }
    if (m==0)
    {
        printf("value of m is 0 \n ", m);
    }
    if (m<0)
    {
        printf("value of m is -1 \n ", m);
    }
}
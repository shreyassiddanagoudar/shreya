#include <stdio.h>
int main(int argc, char*argv[]) {
    int a,b;
    printf("enter the numbers \n");
    scanf("%d %d", &a, &b);
    if((a^b)<0)
    {
        printf("the number are of opposite sign");
    }
    else{
        printf("the number are of same sign" );
    }
    return 1;
}
#include <stdio.h>
int main(int argc,char*argv[]) {
    int n, m, prod = 1;
    printf("Enter the value of n\n");
    scanf("%d",&n);
    
    while(n >0)
    {
    m=n%10;
    prod *= m;
    n=n/10;
    }
    printf("prod is =%d", prod);
    return 0;
}
#include <stdio.h>
int main(int argc,char*argv[]) {
    int n, m, sum = 0;
    printf("Enter the value of n\n");
    scanf("%d",&n);
    
    while(n != 0)
    {
    m=n%10;
    sum += m;
    n=n/10;
    }
    printf("sume is =%d", sum);
    return 0;
}
#include <stdio.h>
int main(int argc,char*argv[]) {
    int n,sum=0;
    printf("Enter the number to find the sum of natural numbers of n\n");
    scanf("%d", &n);
    for(int i=1; i<=n; i++ ) {
        sum+=i;
    }
    printf("%d \n",sum);
}
#include <stdio.h>
int main(int argc,char*argv[]) {
    int n, fact=1;
    printf("Enter the value of n\n");
    scanf("%d", &n);
    
    
        for(int i=1; i<=n; i++ ) {
        fact *= i;
    }
    printf("%d =%d", n, fact);
return 0;
}
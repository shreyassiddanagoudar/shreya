#include <stdio.h>
int main(int argc,char*argv[]) {
    int n,m,i, rev =0;
    printf("Enter the number to rev n: \n");
    scanf("%d", &n);
    while(n !=0) {
        m= n%10;    
        rev = rev*10 + m;
        n /=10;
       
        }
       
    printf("%d \n",rev);
}
#include <stdio.h>
int main(int argc,char*argv[]) {
    int n, count=0;
    printf("Enter the digit \n");
    scanf("%d", &n);
    while( n>0) {
        n=n/10;
        count++;
        }
         printf("%d \n",count);
        
    
}
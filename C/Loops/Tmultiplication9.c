#include <stdio.h>
int main(int argc,char*argv[]) {
    int n;
    printf("Enter number to create a multiplacation table\n");
    scanf("%d", &n);
    for(int i=1; i<=10; i++ ) {
         
        printf("%dX%d=%d \n",n,i,n*i);
       
    }
    
}
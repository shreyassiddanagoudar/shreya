#include <stdio.h>
int main(int argc,char*argv[]) {
    int n,a,i,sum=0;
    printf("Enter the number to find the sum of natural numbers of n\n");
    scanf("%d", &n);
    for(int i=1; i<=n; i++ ) {
         
         if(i%2==0){
              sum+=i;
       
        }
       
    }
    printf("%d \n",sum);
}
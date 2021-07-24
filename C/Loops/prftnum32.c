#include<stdio.h>
int main (int argc, char*argv[]) {
    int n, sum=0; 
    printf("Enter the number:");
    scanf("%d", &n);

    
    for (int i=1; i<=n/2; i++) {
        if(n%i==0){
            sum+=i;
        }
    }
       

    if (n==sum){
    printf("the given value is a perfect number", n);
    }
    else {
        printf("the given value is not a perfect number", n);
    }
}
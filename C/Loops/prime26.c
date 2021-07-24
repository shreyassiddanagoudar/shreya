#include<stdio.h>
int main(int argc,char*argv[]) {
    int n, i, flag=0;
    printf("Enter the number\n");
    scanf("%d", &n);

    for (int i=2; i<=n/2; ++i) {
        if (n%i ==0) {
            flag =1;
            break;
        }
         //else
            //printf("prime no\n");
    }
    if (n==1) {
        printf("1  is either prime nor composite\n ");
    }
    else{
            if (flag==0) 
                printf("%d is a prime number\n", n);
            
            else 
                printf("%d is not a prime number/n",n);
    }
            
}
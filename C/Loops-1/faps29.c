#include<stdio.h>
int main(int argc,char*argv[]) {
    int n,a, flag, sum=0;
    printf("Enter the number:\n");
    scanf("%d",&a);
    for(int i=2; i<=a/2; i++) {
    flag=1;
    for(int j=2; j<=i/2; j++) {
        if (i%j==0) {
            flag=0;
            break;
        }
    }    
    if(flag==1 && a%i==0) {
        printf("%d\n", i);
    }
}
}

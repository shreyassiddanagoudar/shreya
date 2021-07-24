#include<stdio.h>
int main(int argc,char*argv[]) {
    int num;
    
    printf("Enter the number");
    scanf("%d", &num);

    for(int i=1; i<=num; i++) {
     if (num % i == 0) {
         printf("%d\n", i);
     }

    }
}
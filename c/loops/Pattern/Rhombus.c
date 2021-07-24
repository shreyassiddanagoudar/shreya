#include<stdio.h>
int main(int argc, char*argv[]) {
    
    for(int i=1; i<=5; i++) {
    for (int j=1; j<=5-i+1; j++) {
         printf(" ");
    }
        for (int k=1; k<=2*i-1; k++) {
       
            printf("*");
    }
   
    printf("\n");
    }
    for(int i=1; i<=5; i++) {
    for (int j=1; j<=i; j++) {
         printf(" ");
    }
        for (int k=1; k<=(11-2*i); k++) {
       
            printf("*");
    }
   
    printf("\n");
    }
    return 1;
}
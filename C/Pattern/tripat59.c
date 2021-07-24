#include<stdio.h>
int main(int argc,char*argv[]) {
    int i,j,k, rows;
    printf("Enter the number of rows:");
    scanf("%d", &rows);
   
    for( int i=rows; i>=1; i--) {
         for(int j=rows-i+1; j>=1; j--) {
             printf(" ");
            }
             for( int k=(2*i-1); k>=1; k--) {
             
                printf("*");
            }
        printf("\n");
    }
     return 0;
}
#include<stdio.h>
int main(int argc,char*argv[]) {
    int i,j,k, rows, column;
    printf("Enter the number of rows:");
    scanf("%d", &rows);
    printf("Enter the number of column:");
    scanf("%d", &column);
    
    
    for( int i=1; i<=rows; i++) {
         for(int j=1; j<=rows-i; j++) {
             printf(" ");
            }
           for( int k=1; k<=column; k++) {
                printf("*");
            }
       printf("\n");
    }
   return 0;
}
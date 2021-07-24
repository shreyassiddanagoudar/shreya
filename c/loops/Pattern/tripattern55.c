#include<stdio.h>
int main(int argc,char*argv[]) {
   int i,j,rows;
    printf("Enter the number of rows:");
    scanf("%d", &rows);

    for(int i=1; i<=rows; i++) {
        for( int j=1; j<=i; j++) {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}
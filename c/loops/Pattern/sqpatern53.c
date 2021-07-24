#include<stdio.h>
int main(int argc,char*argv[]) {
    int i,j, rows;
    printf ("Enter the number of rows:");
    scanf("%d :\n", &rows);
    
    for (int i=1; i<=rows; ++i) {
        for(int j=1; j<=rows; ++j) {
            printf ("*");
        }
        printf ("\n");
    } 
    return 0;
}
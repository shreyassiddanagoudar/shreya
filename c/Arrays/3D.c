#include<stdio.h>
int main(int argc, char*argv[]) {
    int a[2] [3][4];
    for(int i=0; i<2; i++) {

    for(int j=0; j<3; j++) {

    for(int k=0; k<4; k++) { 

    
    printf("enter the values :");
    scanf("%d", &a[i][j][k]);
    }
    }
    }
    for(int i=0; i<2; i++) {

    for(int j=0; j<3; j++) {

    for(int k=0; k<4; k++) { 
    
    printf("%d %d %d", a[i] [j] [k]);
    }
    }
    }
    
}
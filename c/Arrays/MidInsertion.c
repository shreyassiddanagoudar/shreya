#include<stdio.h>
int main(int argc, char*argv[]) {
    int a[5]={1, 2, 3};
    int x=40;
    int size=3;
    int i;
    
    for(int i=4; i>size/2; i--) 
        a[i]=a[i-1];
        a[size/2]=x;
    for(int i=0; i<5; i++) 
        printf("%d ",a[i]);
        printf("\n");

    return 0;
}
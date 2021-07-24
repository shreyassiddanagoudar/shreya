#include<stdio.h>

int main(int argc, char*argv[]) {
    int a[7]={1, 2, 3, 4, 5};
    int x=7;
    int size = 5;
    for(int i=6; i>size; i--) {
        a[i] = a[i-1];
        a[size] = x;
    }
    for(int i=0; i<6; i++) {
        printf("%d ", a[i]);
        printf("\n");
    }
    return 0;
}
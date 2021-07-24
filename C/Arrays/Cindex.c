#include<stdio.h>
int main(int argc, char*argv[]) {
    int a[4]={1, 3, 2, 4};
    int b[5]={4, 6, 3, 1, 8};
    int c[9];
    int cindex=0;
    for(int i=0; i<4; i++) {
        c[cindex]=a[i];
        cindex++;
    }
     for(int i=0; i<5; i++) {
        c[cindex]=b[i];
        cindex++;
     }
    for(int i=0; i<cindex; i++) {
        printf("%d ", c[i]);
    }
}

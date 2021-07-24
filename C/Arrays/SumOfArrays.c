#include<stdio.h>
int main(int argc, char*argv[]) {
    int a[4]={1, 5, 3, 2};
    int sum=0;
    for (int i=0; i<4; i++) {
        sum +=a[i];
    }
    printf("the sum of the elements are %d\n", sum);
}
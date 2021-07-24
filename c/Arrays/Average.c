#include<stdio.h>
int main(int argc,char*argv[]) {
    int a[9]= {1, 3, 2, 4, 5, 7, 6, 8, 9 };
    int Avg = 0;
    int sum = 0;

    for (int i=0; i<9; i++) {
        sum +=a[i];
        Avg = sum/9;

    }
    printf("%d \n", Avg);
}
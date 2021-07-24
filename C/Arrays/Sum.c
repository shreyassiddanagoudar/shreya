#include<stdio.h>
int main(int argc,char*argv[]) {
    int a[5] = {1, 2, 5, 6, 8}; //store the elements in an aray of size 5 with length of values 
    int sum=0;

    for(int i=0; i<5; i++){
        sum +=a[i]; //initializwd with the sum
    }
    printf("%d \n", sum);
}

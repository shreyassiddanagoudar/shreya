#include<stdio.h>
int main(int argc,char argv[]) {
    int a[6] = {2, 3, 6, 7, 8, 9};//stored the array size of 6 with lenght in brackets
    
    for(int i=6-1; i>=0; i--) { //reverse value condition
        printf("%d \n",a[i]); //stored and printed the reverse values
    }
    }
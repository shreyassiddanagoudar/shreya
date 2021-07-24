#include<stdio.h>
int main(int argc,char*argv[]) {
    int a[6] = {2, 3, 6, 7, 8, 9};//store elements in an  array of size 6 with lenght in brackets
    
    for(int i=6-1; i>=0; i--) { //reverse value condition
        printf("%d \n",a[i]); //stored and printed the reverse values
    }
    }
#include<stdio.h>
int main(int argc, char*argv) { //creating the main function
    int a[5]={1, 2, 3, 4, 5}; //storing the values
    int b[4]={5, 6, 7, 8,};
    int i; //declaring
    int c[9];//storing
    for( i=0; i<5; i++) {
            c[i]=a[i];
        }
        int k=i;
        // printf("k=%d",k);
        for(int i=0; i<4; i++) {
            c[k]=b[i];
            k++;
        }
        printf("The merjed value\n ");
         for(int i=0; i<9; i++) {
             printf("%d\n", c[i]);
            
        }
    
}
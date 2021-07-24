#include<stdio.h>
int main(int argc, char*argv[]) {
    int a[5]={1, 2, 3, 4, 5};
   
    int position=4;
    int i;
    int n;
    
    for(int i=0; i<position/2; i++) 
        a[position]=a[3];
        a[3]=3;
      
    for(int i=0; i<5; i++) 
        printf("%d ",a[i]);
        printf("\n");

    return 0;
}
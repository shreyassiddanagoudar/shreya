#include<stdio.h>
int main(int argc, char*argv[]) {
    int a[5]={1, 2, 3, 4, 5};
   
    //int position;
    int i;
    int n;
    
   // for(int i=position-1; i>position-1; i--) 
     //   a[i]=a[i];
      
    for(int i=1; i<5; i++) 
        printf("%d ",a[i]);
        printf("\n");

    return 0;
}
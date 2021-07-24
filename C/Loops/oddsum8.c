#include <stdio.h>
int main(int argc,char*argv[]) {
    int n,sum=0;
    
    for(int i=1; i<=100; i++ ) {
         
         if(i%2){
              sum +=i;
       
        }
       
    }
    printf("%d \n",sum);
}
#include <stdio.h>
int main(int argc,char*argv[]) {
    int n, flag;
    printf("Enter the value of n\n");
    scanf("%d", &n);
    for(int i=1; i<=n; i++ ) {
         flag=0; 
         for(int j=1; j<=n; j++ ) {
             if(i%j==0) 
                 flag++;
         }
        if (flag==2)
            printf ("%d\n", i);
        
        
    }
}
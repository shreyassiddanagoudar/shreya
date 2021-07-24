#include <stdio.h>
int main(int argc,char*argv[]) {
    int n, flag, sum=0,i;
    printf("Enter the value\n");
    scanf("%d", &n);

    for(int i=2; i<=n; i++) {
        flag=1;
        for (int j=2; j<=i/2; j++) {
            if (i%j==0) {
                flag=0;
                break;
            }
           

        }
       
    if(flag==1) {
        printf("%d\n", i);
        sum +=i;
        //printf("%d\n", sum);
      

    }
 
}
printf("%d", sum);
}

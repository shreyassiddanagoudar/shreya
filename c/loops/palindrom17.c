#include <stdio.h>
int main(int argc,char*argv[]) {
    int n,m, revd =0, oN;
    printf("Enter the palendrome sequence n: \n");
    scanf("%d", &n);
    oN =n;
    while(n !=0) {
        m= n%10;    
        revd = revd*10 + m;
        n /=10;
       
        }
       if (oN == revd)
       {
    printf("%d is a palendrom\n",oN);
       }
    else {
        printf("%d is not a palendrom\n",oN);
    }
}
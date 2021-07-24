#include<stdio.h>
int main(int argc, char*argv[]) {
    int n,m, hcf;
    printf("HCF of two numbers\n");
    printf("Enter the number:\n");
    scanf("%d %d", &n,&m);
    printf("Numbers are %d %d", n,m);

     int least = n>m ? m:n;
    int cnt = least/2;
    for ( int i=1; i<cnt; i++) {
        if (n%i==0 && m%i==0) {
            hcf = cnt;
        } 
        printf("hcf of %d and %d are %d\n", n,m,hcf);
    }
}
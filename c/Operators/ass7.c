#include <stdio.h>
int main(int args, char*argv[]) {
    
    int a,b,c;
    printf ("Enter the value for a=\n");
    scanf("%d %d %d", &a,&b,&c);
   
    printf("value of i is %d\n", a>b && a>c);
     printf("value of j is %d\n", a>b || a>c);
     printf("value of k is %d\n", a>b && b>c);
     printf("value of l is %d\n", a>b || b>c);
     printf("value of m is %d\n", a<b && a<c);
     printf("value of n is %d\n", a<b || a<c);
     printf("value of o is %d\n", a<b && b<c);
     printf("value of p is %d\n", a>b || b>c);
     printf("value of q is %d\n", a==b && a<c);
     printf("value of r is %d\n", a==b || a<c);
     printf("value of s is %d\n", a==b && b>c);
     printf("value of t is %d\n", a==b || b>c);
     printf("value of u is %d\n", a==b && b==c);
     printf("value of v is %d\n", a!=b && b==c);
     printf("value of w is %d\n", a!=b && a!=c);
}
    
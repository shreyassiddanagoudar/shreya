#include <stdio.h>

int main(int args, char*argv[]) {
    
    char a,b;
    printf ("Please enter the value for a and b\n");
    scanf ("%c %c", &a,&b);
  //  printf ("Please enter the value for b=\n");
   // scanf ("%c", &b);
    printf ("a==b %d\n", a==b);
    printf ("a!=b %d \n", a!=b);
    printf ("a>b %d \n", a>b);
    printf ("a<b %d \n", a<b);
    printf ("a>=b %d \n", a>=b);
    printf ("a<=b %d \n", a<=b);

}
#include <stdio.h>

int main(int argc, char*argv[]) {
 char b,a;
 
 printf ("Enter two character:");
 scanf ("%c %c", &b,&a);
 printf ("%c = %d \n", a,a);
 printf ("%c = %d \n", b,b);
 printf ("%c %c = %d %d \n", a,b,a+b,a+b);
 printf ("%c %c = %d %d \n", a,b,a-b,a-b);
 printf ("firdt char = %c, second char = %c, ascii adition value is %dand ascii code is %c\n ", a,b,a+b,a+b);

}
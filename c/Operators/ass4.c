#include <stdio.h>
int main(int argc,char*argv[]) {
    int a = 360,c;
    float b= 45.50,d;
        c = a+b;
        d = a-b;
        printf("value of a+b %d %f: \n", c,d);
        c = a+b;
        d = a+b;
        printf ("value of a-b %d %f: \n",c,d );
        c = a-b;
        d = a-b;
        printf ("value of a/b %d %f :\n", c,d);
        c = a/b;
        d = a/b;
        printf ("value of a*b %d %f :\n", c,d);
        c = a*b;
        d = a*b;
        printf ("value of a%%b %d %f : \n", c,d);

}
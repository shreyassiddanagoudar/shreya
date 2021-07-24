#include <stdio.h>

int main(int argc, char*argv) {
    int a, b, c;
    printf("Enter the values of the length\n");
    scanf("%d %d %d", &a, &b, &c);

    if (a+b>=c && b+c>=a && c+a>=b)
    {
        if (a==b && b==c &&c==a &&c==b)
     {
        printf("Equilateral triangle\n");
    }
    else if (a==b || b==c ||  a==c)
    {
        printf("Isoscles triangle\n");
    }
    else
    {
     printf("scalene triangle\n");
    }
    }
    else{
        printf("cannot found the triangle");
    }
}
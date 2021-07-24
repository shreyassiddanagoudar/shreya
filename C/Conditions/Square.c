#include <stdio.h>

int main(int argc, char*argv) {
   
   int a,b;
    printf("Enter the length of a rectange \n");
    scanf("%d", &a);
    printf("Enter the breadth of a rectangle \n");
    scanf("%d", &b);

    if(a==b)
    {
    printf("The given number is a square \n");
    }
    else 
    {
    printf("The given number is not a square \n");
    }
    }
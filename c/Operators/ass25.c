#include<stdio.h>

int main(int argc, char*argv[]) {
    int a,b;
    printf("Enter the numbers \n");
    scanf("%d %d" , &a,&b);
    printf("the numbers are same %d", a==b);
    printf ("the difference between two numbers is %d", a-b);
    return 1;
    
}
#include<stdio.h>
int main(int argc, char*argv[]) {

    for (int i = 0; i <=5; i++)
    {
        for (int j = 0; j<=i; j++)
        {
            printf("*");
            printf(" ");
        }
    printf("\n");
    }

    return 1;
}
#include <stdio.h>

int main(int argc, char*argv[]) {
    int a,b,c;
    float sum, total;
    printf("Enter the number\n");
    scanf("%d %d %d", &a, &b, &c);
    sum = (b*b) - (4*a*c)/(2*a);
    if (sum<0)
    {
        printf("The total is %f %f \n", ((-b-total)/2*a), (-b+total)/2*a );
    }
        else 
        {
        printf("Its is not possible to get the roots\n");
    }

}
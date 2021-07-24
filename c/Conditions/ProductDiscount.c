#include <stdio.h>

int main(int argc,char*argv[]) {
    int sum,dis;
    printf("Enter the number of quantities \n");
    scanf("%d",  &sum);
    dis = (sum*0.9);
    
    if (sum > 1000)
    {
        printf("The overall discount on the product is %d\n ", dis);
    }
    else
     printf("The product does not holds the discont %d\n ", dis);
}
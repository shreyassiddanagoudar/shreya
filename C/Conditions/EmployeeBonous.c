#include <stdio.h>

int main(int argc,char*argv[]) {
    int year, salary, service;
    printf("Enter the employee year of service \n");
    scanf("%d",  &year);
    printf("Enter employee salary \n");
    scanf("%d",  &salary);
    service = salary* 0.05;
    if (year > 5)
    {
        printf("The net bonous amount is %d\n ", service);
    }
    else
    {
     printf("No bonous amount is issued %d\n ", service);
    }
}
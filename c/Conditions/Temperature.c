#include <stdio.h>

int main(int argc,char*argv[]) {
    int temp;
    printf("Enter the temp : \n");
    scanf("%d",  &temp);

if (temp<0)
{
    printf("freezing weather\n", temp);
}   
    else if (temp>=0 && temp<=10)
    {
    printf("very cold weather\n", temp);
    }   
        else if (temp>=20 && temp<=30)
        {
        printf("cold weather\n", temp);
        }   
            else if (temp>=30 && temp<=40)
            {
            printf("hot weather\n", temp);
            }  
                else if (temp>=40)
                {
                printf("very hotweather\n", temp);
                }    
}
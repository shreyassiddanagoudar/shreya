#include <stdio.h>

int main(int argc,char*argv[]) {
    int m;
    printf("Enter the height of a person: \n");
    scanf("%d",  &m);

    if (m>=0 && m <=100)
    {
        printf("person in dwarf catagory\n ");
    }
       else if (m>=101 && m<=150)
        {   
        printf("person in short catagory \n ");
         }
           else if (m>=151 && m<=165)
            {
            printf("person in medium catagory \n ");
            }
              else {                
                printf("person in tall catagory \n ");
                }
}
#include <stdio.h>

int main(int argc,char*argv[]) {
    int x,y;
    printf("Enter the coordinate points: \n");
    scanf("%d %d",  &x, &y);

    if (x>0 && y>0)
    {
        printf("The point lies in 1st Quadrant ", x,y);
    }
        else if (x>0 && y<0)
        {
       printf("The point lies in 2nd Quadrant ", x,y);
        }
            else if (x<0 && y<0)
            {
             printf("The point lies in 3rd Quadrant ", x,y);
            }
                else if (x<0 && y>0)
                {
                 printf("The point lies in 4th Quadrant ", x,y);
                }
}
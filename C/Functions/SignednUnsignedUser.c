# include <stdio.h>

 int main() {

            short x;
            signed short y;
            unsigned short z; 

printf("enter the number\n");
scanf("%d %hi %hu",&x, &y, &z);

    printf("value is is %hu, %d \n",  z, sizeof(unsigned short));
    printf("value is is %hi, %d \n",  y, sizeof(signed short));
    printf("value is is %hu, %d \n",  x, sizeof(short));

printf("enter the number\n");
scanf("%d %li %lu",&x, &y, &z);
   
    printf("value is is %li, %d \n",  y, sizeof(signed long));
    printf("value is is %lu, %d \n",  z, sizeof(unsigned long));
    printf("value is is %lu, %d \n",  x, sizeof(long));

printf("enter the number\n");
scanf("%d %f %lf",&x, &y, &z);
    
    printf("value is is %f, %d \n",  x,y,z,sizeof(float));
    printf("value is is %lf, %d \n", x,y,z,sizeof(double));

 }
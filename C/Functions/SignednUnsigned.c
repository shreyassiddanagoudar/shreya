# include <stdio.h>

 int main() {
  
            short ia = 2;
            signed short ib =-34;
            unsigned short ic =45;

    
    printf("value is is %hi, %d \n",  ia, sizeof(short));
    printf("value is is %hu, %d \n",  ib, sizeof(signed short));
    printf("value is is %hu, %d \n",  ic, sizeof(unsigned short));
            
            short la = 355;
            signed short lb =55.5;
            unsigned short lc =65.5;

    printf("value is is %li, %d \n",  la, sizeof(long));
    printf("value is is %lu, %d \n",  lb, sizeof(signed long));
    printf("value is is %lu, %d \n",  lc, sizeof(unsigned long));

            short a = 57.55;
            signed short b =-8.5;
            unsigned short c =7678.9797;

    printf("a,b,c, adress is %p and value is is %f, %d \n",  a,b,c,sizeof(float));
    printf("a,b,c, adress is %p and value is is %lf, %d \n", a,b,c,sizeof(double));
   
}
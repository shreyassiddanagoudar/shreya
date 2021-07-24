#include <stdio.h>

int main(int argc, char*argv[]) {

int pcm, comb;
printf("Enter the number\n");
scanf ("%d %d", &pcm, &comb);

if( pcm >=55 && comb <=175) 
{
printf("The student is elligible\n");
}
else 
{
printf ("The student is not elligible");
}
}
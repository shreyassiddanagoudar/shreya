#include <stdio.h>
int main(int argc,char*argv[] ) {
int input, firstnum, lastnum;
printf("Enter the  num");
scanf("%d\n", &input);

firstnum =input/10;
lastnum = input%10;

while(firstnum>=10)
{
    firstnum = firstnum / 10;
}
printf("%d + %d = %d\n", firstnum,lastnum, firstnum+lastnum);

}
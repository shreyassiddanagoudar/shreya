#include <stdio.h>
#include <stdbool.h>

int main(int argc, char * argv[]) {

char ch;
ch= 'A';
printf("value is %c size is %d\n",ch, sizeof(char) );

bool bh;
bh= 0;
printf("value is %d size is %d\n", bh,sizeof(bool));

char name[456] = "shreya";
printf("value is %s size is %d\n", name, sizeof(char));

}

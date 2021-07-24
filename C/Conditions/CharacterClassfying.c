#include <stdio.h>

int main(int argc, char*argv[]) {

char ch;
printf("Enter the character/n");
scanf("%c", & ch);
if (ch>='a' && ch<='z' ||ch>='A' && ch<='Z') 
{
    printf ("The given character is alphabet\n");
}
else if (ch>='0' && ch<='9') 
{
    printf ("The given character is digit\n");
}
else
{
    printf ("The given character is special character\n");
}
}

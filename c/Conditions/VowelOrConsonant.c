#include <stdio.h>

int main(int argc, char*argv[]) {

char ch;
printf("Enter the character/n");
scanf("%c", & ch);
if (ch=='a' || ch=='e' || ch=='i' ||  ch=='o' || ch=='u' || ch=='A' || ch=='E' || ch=='I' ||  ch=='O' || ch=='U' ) 
{
    printf ("The given character is a vowel\n");
}
else
{
    printf ("The given character is a consonant\n");
}
}
#include <stdio.h>

int main(int argc, char*argv[]) {

    char ch;
    printf("Enter the grade\n");
    scanf("%c", &ch);
    switch(ch) {
        case 'E' :printf ("excilent");
        break;
        case 'V' :printf ("Very good");
        break;
        case 'G' :printf ("good");
        break;
        case 'A' :printf ("average");
        break;
        case 'F' :printf ("fail");
        break;
        default: printf("invalid inputs");
        break;
    }
}
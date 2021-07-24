#include <stdio.h>

int main(int argc, char*argv[]) {

    char ch;
    printf("Enter the digit\n");
    scanf("%c", &ch);
    switch(ch) {
        case '1' :printf ("hello");
        break;
        case '2' :printf ("good");
        break;
        case '3' :printf ("morning");
        break;
        case '4' :printf ("welcome");
        break;
    
        default: printf("invalid inputs");
        break;
    }
}
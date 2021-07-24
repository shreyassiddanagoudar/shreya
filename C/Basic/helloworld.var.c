/*
    Simple HELLO WORLD program
    ITfyMe
*/

// include library
#include <stdio.h>

int main(int agrc, char *argv[]) {
    char name[128];//place holder to keep the name
    printf("please enter your name\n");
    scanf("%s", name);//system call which accepts the name and store in "var"
    printf ("Hello %s ! Welcome to programing world \n", name) ;
}
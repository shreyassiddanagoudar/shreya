#include<stdio.h>
#include<string.h>

int main() {
    char str1[20]="shreya";
    int i=0;
    while (str1[i]!='\0') {
        i++;
    }
    printf("%d", i);
}
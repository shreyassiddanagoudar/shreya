#include<stdio.h>
#include<string.h>

int main() {
    char str1[] ="hloo";
    char str2[20];
    int i=0;
    while (str1[i]!='\0') {
        str2[i]=str1[i];
        i++;
    }
    printf("%s",str2);
}
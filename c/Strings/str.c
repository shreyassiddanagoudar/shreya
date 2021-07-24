#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main() {
    char str1[] ="this is";
    char str2[50] = "shreya";
    int i=0; 
    // char k[i]=0;
   while (str1[i] || str2[i] !='\0'){

     str1[i]+str2[i];
     i++;
    }
     printf("%s %s", str1, str2);
    // printf("%s", str2);
    return 0; 
}
#include<stdio.h>

int cntxtoy(char s[], int i, int size) {
    if(i ==size)  {
    return 0;    }
    if(s[i] == 'x') {
        return (s[i]='y') + cntxtoy(s, i+1, size);
    }
    else {
        return  cntxtoy(s, i+1, size);
    }
}

int main() {
    int i=0, size;
    char s[128];
    printf("Enter the string to check the lowercase appearence \n");
    scanf("%s", &s);
    printf("enter the size of the string ");
    scanf("%d",&size);
    cntxtoy(s,i,size);
    printf("Number of appearance of s is %s", s);
}
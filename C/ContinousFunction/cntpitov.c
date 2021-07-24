#include<stdio.h>
#include<string.h>

int cntpitov(char s[], int i, int size) {
    if(i ==size-1)  {
    return 0;    }
    if(s[i] == 'p' && s[i+1] == 'i') {
         s[i]='3';
        s[i+1]='.';
        s[i+2]='1';
       return s[i+3]='4' + cntpitov(s, i+1, size);
    }
    else {
        return  cntpitov(s, i+1, size);
    }
}

int main() {
    int ans, i=0, size;
    char s[128];
    printf("Enter the string to check the lowercase appearence \n");
    scanf("%s", &s);
    printf("enter the size of the string ");
    scanf("%d",&size);
    cntpitov(s,i,size);
    printf("Number of appearance of s is %s", &s);
}
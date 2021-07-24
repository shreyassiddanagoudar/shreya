#include<stdio.h>

int cnthi(char s[], int i, int size) {
    if(i ==size-1)  {
    return 0;    }
    if(s[i] == 'h' && s[i+1] == 'i') {
        return 1 + cnthi(s, i+1, size);
    }
    else {
        return  cnthi(s, i+1, size);
    }
}

int main() {
    int ans, i=0, size;
    char s[128];
    printf("Enter the string to check the lowercase appearence \n");
    scanf("%s", &s);
    printf("enter the size of the string");
    scanf("%d",&size);
    ans= cnthi(s,i,size);
    printf("Number of appearance of s is %d", ans);
}
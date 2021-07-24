#include<stdio.h>

int cntx(char s[], int i, int size) {
    if(i ==size-1)  {
    return 0;    }
    if(s[i] == 'x') {
        return 1 + cntx(s, i+1, size);
    }
    else {
        return  cntx(s, i+1, size);
    }
}

int main() {
    int ans, i=0, size;
    char s[128];
    printf("Enter the string to check the lowercase appearence \n");
    scanf("%s", &s);
    printf("enter the size of the string ");
    scanf("%d",&size);
    ans= cntx(s,i,size);
    printf("Number of appearance of s is %d", ans);
}
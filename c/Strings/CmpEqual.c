#include<stdio.h>
void main() {
    char str1[]="hello";
    char str2[]="hrllo";
    int cmp=0;
    int cnt=0;
    while (str1[cnt] || str2[cnt] !='\0') {
        if(str1[cnt] !=str2[cnt]) {
            cmp=1;
            break;
        }
        cnt++;
    }
    if(cmp==0){
        printf("string is equal");
    }
    else {
        printf("string is not equal");
    }
    
}
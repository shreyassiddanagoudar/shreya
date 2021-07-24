#include<stdio.h>
#include<string.h>

int main() {
    char str=0;
    char substr=0;
    int index;
    while (strs[str] !='\0' && subs[substr] !='\0') {
        if (substr ==0) {
            index = str;
        }
        if(subs[substr] == strs[str]) {

           substr++;
        }
        else {
            substr=0;
        }
    
         substr++;
    }
     if((str[substr] == '\0' &&substr ==0) || subs[substr])!='\0') {
         return -1;
        }
        else {
            return index;
        }
}
void main() {
    char str[]="xyz";
    char subs[]="abc";
    int index=substring(str);
}
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void sttok(char str[], char stoken) {
    int i=0, tcnt=0;
    int len=strlen(str);
    char token[1023];

    for(i=0; i<len; i++) {
        if(str[i] == stoken) {
            token[tcnt] ='\0';
            printf("%s\n",token);
            tcnt=0;
        }
        else {
            token[tcnt]=str[i];
            tcnt++;
        }
    
    }
    printf("%s\n",token);

}
int main() {
    char str[]="hello how are you my friend";
    char stoken = ' ';
    sttok(str, stoken);
}
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void wordBuil(char a[10][10],int r,int c) {
    char d='A';
    for(int i=0; i<r; i++) {
        for(int j=0; j<c; j++) {
            a[i][j] = d+ rand ()% 26;
        }
    }
}
void addWordsToMatrix(char s[10][10], int c, int r) {
    char words[5][10] = {"SHREYA", "REYA", "SASH", "MEESHA", "teya"};
    for(int i=0; i<5; i++) {
        int ro= rand() % r;
        printf("word is %s to be inserted in rows %d\n", words[i],ro);
        int co = rand() %(c-strlen(words[i]));
        for(int j=0; j<strlen(words[i]); j++) {
            s[ro][co+j]= words[i][j];
        }
    }
}
void printArray(char s[10][10], int r, int c) {
    for (int i =0; i<r;i++) {
        for (int j =0; j<c;j++) {
            
        printf("%c ", s[i][j]);

    }
   
    printf("\n");
    }
}
int main() {
    char s[10][10];
    // fileMatrix(s,10,10);
    // printMatrix(s,10,10);
    wordBuil(s,10,10);
    addWordsToMatrix(s,10,10);
    printArray(s,10,10);
    return 0;  
}


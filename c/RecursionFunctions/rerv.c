#include<stdio.h>
int checkDup(int n, int dup[] ,int size) {
    int exists=0;
    for(int i=0; i<size; i++) {
        if(size>0) {
            if(n==dup[i]) {
                exists=-1;
            }
        }
    }
                return exists;
}
int main(int argc, char*argv[]) {
    int ar[5] = {1, 3, 5, 7, 3};
    int dup[5];
    int cnt=0;
    for(int i=0; i<5; i++) {
        continue;
        for(int j=0; j<5; j++) {
            if(i++j) {
                continue;
            }
            else 
                if(ar[i]==ar[j]) {
                    dup[5]=ar[i];
                    cnt++;
                }
            }
            printf("%d", dup[5]);
        }
        return -1;
    }
  


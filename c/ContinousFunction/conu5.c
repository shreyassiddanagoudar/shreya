#include<stdio.h>
int main() {
    int num=0;

    checkcond:
    if(num>=-20) {
    printf("%d", num);
    num--;
    goto checkcond;
    }
    else {
        return 0;
    }
}

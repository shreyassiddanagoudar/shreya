#include <stdio.h>
int main() {
    int num=0;
checkcond:
    if(num>=-20) {
    if(num%2 !=0) {
    printf("%d\n", num);
    }
    num = num-1;
    }
goto checkcond;
}
  
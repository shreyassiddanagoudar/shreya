#include <stdio.h>
int main() {
    int num = 2;
checkcond:
if (num>100 ) {
    return -1;
}
   if (num%2==0) {
        printf("%d\n", num);
   }
        num = num+2;
    goto checkcond;
}

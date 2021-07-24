#include <stdio.h>
#include "itmath.h"
int main() {
    
    int armstrong =isArmStrong(145);
    if (armstrong==1) {
        printf("number is armstrong");
    }
    else {
        printf("number is not armstrong");
    }
}
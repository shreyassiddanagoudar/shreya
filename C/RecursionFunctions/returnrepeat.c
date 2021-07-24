#include<stdio.h>

int repeat(int num, int b) {
    if(num==0) {
        return 0;
    }
    else {
    int digit =num%10;
    return (digit == b)+repeat(num/10, b);
    }
}

int main() {
    int b, num;
    printf("Enter the the number: ");
    scanf("%d ", &b);
    int ans = repeat(12242, b);
    printf("The repeated number count is %d", ans);
}
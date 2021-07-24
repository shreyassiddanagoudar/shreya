#include<stdio.h>

int bare(int b, int r) {
    if(r==0) {
        return 1;
    }
    else {
        return b * bare(b, r-1);
    }
}

int main() {
    int ans, b, r;
    printf ("Enter the base value b:");
    printf("Enter the raise value r:");
    scanf("%d %d", &b, &r);
    ans = bare(b, r);
    printf("The base raise is %d", ans);
}
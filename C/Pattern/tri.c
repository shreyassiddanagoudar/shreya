#include<stdio.h>
int tri(int n) {
    if(n==0) {
        return 0;
    }
    else  {
        return n + tri(n-1);
    }
}

int main() {
    int blocks, n;
    printf("Enter the number of blocks in a row: \n");
    scanf("%d", &n);
    blocks = tri(n);
    printf("Total number of triangle blocks present are %d",  blocks);
}
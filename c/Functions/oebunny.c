#include<stdio.h>

int oebun(int n) {
    if(n ==0) {
        return 0;
    }
    else if(n%2==0) {
        return 3 + oebun(n-1);
    }
    else if (n%2 != 0) {
        return 2 + oebun(n-1);
    }
}

int main() {
    int res, n;
    printf("Enter the number of bunny's in a line: \n");
    scanf("%d", &n);
    res =oebun(n);
    printf ("%d", res);
}
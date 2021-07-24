#include<stdio.h>

int bunny (int n) {
    if(n==0) {
        return 0;
    }
    else {
        return 2+bunny(n-1);
    }
}
int main() {
    int n;
    printf("Enter the number of bunny's: \n");
    scanf("%d",&n);
    int res = bunny(n);
    printf("total number of ears of bunny is %d ", res);
    }
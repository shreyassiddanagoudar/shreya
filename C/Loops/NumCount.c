#include <stdio.h>
int main(int argc,char*argv[]) {
    int n;
    int Count = 0;
    printf("Enter the integer number");
    scanf("%d", &n);
    while (n!=0) {
        n /=10;
        ++Count;
    }
        printf("%d", Count);

}
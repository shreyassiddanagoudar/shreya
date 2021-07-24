#include<stdio.h>

int cnt = 0;
int avgDigit(int n) {
    if (n == 0) {
        return 0;
    }
    cnt++;
         
       return n%10 + avgDigit(n/10);
    
}    

int main () {
    int avg;
    printf("Enter the number:");
    scanf("%d", &avg);
    printf("%d is %f",avg, avgDigit(avg)*1.0/cnt); 
}

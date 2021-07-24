#include<stdio.h>
int main(int argc, char*argv[]) {
    
    int a[7] = {3,2,4,5,7};
    int diff = 0;
    
     for(int i=0; i<7; i++) {
        // int diff = a[i]-i;
        if(a[i]-i !=diff) {
            while(diff<a[i]-i) {
                a[i] = a[i]+diff;
                diff++;
            }
        }
        
        printf("%d", a[i]);
    }
    return diff;
}

#include<stdio.h>
int main(int argc, char*argv[]) {
    int arr[] = {1, 1.5, -3, 3,-1.7, 4};
    int x = 0;
    
    for(int i=0; i<6; i++) {
         int pair = arr[i];
        for(int j=i+1; j<6; j++) {
            if (pair + arr[j] == x){
                printf("(%d %d) ", pair, arr[j]);
            }
        }
    }
}
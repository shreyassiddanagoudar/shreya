#include<stdio.h>
void printArray(int a[], int size) {
    for (int i =1; i<size;i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
}
void missingSort(int a[], int size) {
   int i,j;
   int  diff = a[i]-i;

    for(int i=0; i<size; i++) {
        if(a[i]-i !=diff) {
            // for(int diff = i; diff<a[i]-i; diff++) {
                while (  a[i]-i>diff) {
                a[i] = a[i]+diff;
                // i=i-1;
            }
                diff++;

        }
        // int temp = a[diff];
        // a[diff] = a[i];
        // a[i] = temp;
        a[i+1]=diff;
    }
}
int main() {
    int a[8] = {2,4,6,8,10};
    //  printArray(a,8) ;
    missingSort(a,8);
    printArray(a,8);
}
#include<stdio.h>
int main(int argc, char*argv[]) {
int a[5] = {2, 234, 55,766, 9};
int n, i, b, k, j;
for(int i=0; i<5; i++) {
    for(int j=i+1; j<5; j++) {
        if(a[i] > a[j]) {
            k = a[i];
            a[i] = a[j];
            a[j] = k;
           
        }
       
    }
}
for(int i=0; i<5; i++){
    printf("%d ", a[i]);
}
return 0;
}
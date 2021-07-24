#include<stdio.h>
#include<stdlib.h>
#include<limits.h>

int findMin(int a[], int n) {  //creating a function
int min=INT_MAX; //inbuilt declaring function (its just taking the max value frm the answer(inbuilt max value))
//printf("INT_MAX is %d", min);
for(int i=0; i<n; i++) {
//    printf("%d %d \n", a[i], min);
    if (a[i]<min) {
    min=a[i];
}
}
//printf("returning %d\n", min);
return min;
}

int findMax(int a[], int min) {
    int max=INT_MIN;
    //printf("INT_MIN is %d", min);
    for(int i=0; i<10; i++) {
       // printf("%d %d", a[i], max);
        if (a[i] >max) {
        max=a[i];
    }
    }
    //printf("returning %d\n");
    return max;
}


int main() {
int arr[10];
int n;
int sum=0;
for(int i=0; i<10; i++) {
    arr[i]=rand();
}

for (int i=0; i<10; i++) {
    printf("%d", arr[i]);
    printf("\n");
   
}
printf("minimum value is %d and maximum value is %d /n", findMin(arr,n), findMax(arr,n));
 return 0;
}


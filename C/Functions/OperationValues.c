#include<stdio.h>
int add(int n1 ,int n2) {
        return n1 + n2;
    }
int sub(int n1 ,int n2) {
        return n1 - n2;
    }
int mul(int n1 ,int n2) {
        return n1 * n2;
    }
     float div(int n1 ,int n2) {
        return (n1 / n2) *1.0;
    }
    void printArray(int a[],int size){
        for(int i=0; i<size; i++){
        printf("%d", a[i]);
    }
    }
    int main(int argc, char*argv[]) {
        int a=10,b=20;
        int arr[]={1, 2, 3, 4, 5};
        int c=add(a,b);
        printf("%d-%d=%d\n",a,b,sub(a,b));
       
        printf("%d*%d=%d\n",a,b, mul(a,b));
         
        printf("%d/%d=%f\n",a,b, div (a,b));
        
        printArray(arr,6);
}
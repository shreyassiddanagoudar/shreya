#include<stdio.h>
int main(int argc, char*argv[]) {
    int a[5]= {1, 2, 6 ,7, 9};
    int odd[5];
    int even[5];
    int oddcnt=0;
    int evencnt=0;
     
    for (int i=0; i<5; i++) {
        if (a[i]%2 !=0) {
            odd[oddcnt] =a[i];
             printf("%d ",odd[oddcnt] );
        }
    }
    printf("\n");
   
    for (int i=0; i<5; i++) {
        if (a[i]%2 == 0) {
            even[evencnt]=a[i];
             printf("%d ",even[evencnt] );
        }  
    }
    return -1;
}

           
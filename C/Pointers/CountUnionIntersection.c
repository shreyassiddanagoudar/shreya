#include<stdio.h>

void getUnionandIntersection(int a[], int b[], int size) {
    int index=0;
    int min_count=0;
    int i,j;
    int count, count2=0;

    while(i<=4 ||j<=4){
        if(i==5) {
            union[count]=a[i];
            count++;
            i++;
        }
        else if (j==5) {
            intersection[count2]=b[j];
            count2++;
            j++;
        }
     else if (a[i]<b[j]) {
            a[i]=b[j];
            union = a[i];
            count2++;
            i++;
        }    
        else if(a[i]>b[j]) {
        b[j]=a[i];
        union = b[j];
        count++;
        j++;
        }
        else {
            union[count++]=a[i];
            intersection[count2]=b[j];

        }
    }
    for(int k=0; k<count; k++) {
        printf("%d", union[k]);
    }
    for(int k=0; k<count2; k++) {
        printf("%d", intersection[k]);
    }
}
int main() {
    int a[]={1, 3,5,7,8};
    int b[]={1,2,3,4,9};
    int size = 5;
    getUnionandIntersection(a,b, size);
}
#include<stdio.h>
void getUnionandIntersection(int a[],int b[], int size) {
    int uneon [10];
    int intersection[10];
    int index=0;
    int index2=0;
    int i=0; int j=0;

    while(i<=4 ||j<=4) {
        if(j==5){
            uneon[index]=a[i];
            i++;

        }
        else if(i==5){
            uneon[index]=a[j];
            j++;

        }
        else if(a[i]<b[j]) {
            uneon[index]=a[i];
            index++;
            i++;
        }
        else if (a[i]>b[j]) {
            uneon[index++]=b[j];
            index++;
            j++;
                
        }
        else {
            uneon[index++]=a[i];
            intersection[index2++]=b[j];
        }
    }
    for(int k=0;k<index;k++){
        printf("%d\n",uneon[k]);
    }
    printf("intersection...\n");
    for(int k=0;k<index2;k++){
        printf("%d\n",  intersection[k]);
    }
    

}

int main() {
    int a[]={1, 3,5,7,8};
    int b[]={1,2,3,4,9};
    int size = 5;
    getUnionandIntersection(a,b, size);
}
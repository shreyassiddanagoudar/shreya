#include<stdio.h>
int Majority(int a[], int size){
int max_count= 0,i;
int majority_num=0;

for(int i=0; i<size; i++) {
  int count=0;
  for(int j=0; j<size; j++) {
    if (a[i]==a[j]) {
      count++;
    }
    if (count>max_count) {
      max_count = count;
      majority_num=i;
    }
    // if (max_count>size/2) {
    //   count=a[i];
    // }
  }
  printf("array[%d] majority_num is %d \n",  i, a[majority_num]);
}
  return 0;
}

int main() {
  int a[] = {4, 3, 6, 3, 4, 5, 1};
  int size =7;
  printf("%d", Majority(a, size));
  return 0;
}

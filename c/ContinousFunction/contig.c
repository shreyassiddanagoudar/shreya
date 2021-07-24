#include<stdio.h>
int Contigious(int a[], int size) {
    int current_sum=2;
    int max_sum = 0;

    for(int i=0; i<size; i++) {
    
        max_sum = max_sum+a[i];
      if(current_sum<max_sum) {
          current_sum = max_sum;
      }
      if(max_sum < 0) {
          max_sum = 0;
      }

        printf(" item [%d] current_sum is %d max_sum is %d \n", a[i], current_sum, max_sum);

    }
     return max_sum;
}

int main() {
    int a[] = {2, 3, -6, 9, 6, 8, 1};
    int size = 7;
    printf("[%d] %d", Contigious(a,size));
}

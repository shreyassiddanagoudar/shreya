#include<stdio.h>

int main(int argc, char*argv[]) {
 int a[3][3] = {{1,2},{3,4},{2,9}};
 int b[2][2] = {{5,3},{7,2}};
 int res[2][2];
 int k;
//   res[i][j] = 0;
    for(int i=0; i<2; i++) {
        for(int j=0; j<3; j++) {
            res[i][j]=0;
            for(int k=0; k<2; k++) {
              res[i][j] += a[i][k] * b[k][j];

            }
        }
    } 
    for(int i=0; i<2; i++) {
        for(int j=0; j<3; j++) {
                printf("%d ", res[i][j]);
        }
        printf("\n");
    }
}


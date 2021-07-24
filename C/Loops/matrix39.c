#include<stdio.h>
int main(int argc, char*argv[]) {
    int trans[2][3] = {{3,4,1},{2,7,5}};

    for(int i=0; i<3; i++) {
        for(int j=0; j<2; j++){
            printf("%d ", trans[j][i]);
        }
           printf("\n");
    }
 
}
#include<stdio.h>
#include<stdlib.h>
//#include<memory.h>

// int numbers(int *n, int len) {
//     for (int i=1; i<i; i++){
//     printf("enter the number of elements");
//     scanf("%d \n", i);
//     }
// }
int main() {
    char *b;
    int i;
    // char *i;
    // printf("enter the number of elements\n"); 
     printf("enter the number of elements");
    scanf("%d", &i);
    char *a=(char *) malloc(i * sizeof(char));
    for ( b=a; b<a+i; b++){
    scanf("%c",b);
    scanf("%c",b);
    }
    for(b=a;b<a+i;b++){
        printf("%c",*b);

    }
    
}

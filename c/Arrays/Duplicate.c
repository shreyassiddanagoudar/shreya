#include <stdio.h>

int checkDuplicate(int n, int dup[], int size) {
    printf("checking duplicate for %d with size %d\n", n, size);
    int exists = 0; // indicates if item is there in the duplicate array
    if (size > 0) {
        // check with duplicate array
        for (int j = 0; j < size; j++) {
            if (n == dup[j]) {
                exists = 1 ;
                break ;
            }
        }
    }
    return exists ;
}

// void printDup(int a[], int size) {
//     printf("printing duplicate array with size %d \n", size);
//     for (int j = 0; j < size; j++) {
//         printf("dup[%d] is %d \n", j, a[j]);
//     }
// }

// Check how many numbers are duplicates in an array
// #include <stdio.h>  
int  main() {  
    // step 1 - declare and initialise array
    // data input
    int a[10] = {1,4,5,3,5,4,7,1,2,0} ;

    // data output 
    // number of duplicates
    int numDuplicate = 0;

    // working variable 
    // store duplicate array in a seperate variable
    int dup[10] ;

    // for each element in an array a
    for (int i=0; i<10 ; i++) {
        // printDup(dup,numDuplicate);
        // check if this element is there in the duplicate array
        if (checkDuplicate(a[i],dup, numDuplicate) == 1)
            continue;         
        for (int j = 0; j < 10; j++) {
            if (i == j) // dont compare the same element
                continue ;
            else {
                if (a[i] == a[j]) {
                    dup[numDuplicate] = a[i];
                    numDuplicate++;
            
                }
            }
        }
    }
    printf("number of dupicate items are %d \n", numDuplicate);
}
   
#include <stdio.h>
#include <string.h>
int cnt=0;

void swap(char *ch1, char *ch2) {
    char tmp;
   printf("c1=%c\n",*ch1);
    printf("c2=%c ",*ch2);
    tmp = *ch1;
    *ch1 = *ch2;
    *ch2 = tmp;
}

void perm(char *array, int start, int end) {
   int i;
   if (start == end){
      printf("s=%d e=%d  ",start,end);
         printf("  %s \n", array);

     cnt++;
   }
   else {
       for (i = start; i <= end; i++) {
          printf("a=%s    ",array);
          swap((array+start), (array+i));
         printf("a=%s",array);
          perm(array, start+1, end);
          swap((array+start), (array+i)); // swap back 
       }
   }
}
 
int main(int argc, char *argv[]) {
    int n = strlen(argv[1]);
    printf(" The permutations of the string are : \n");
    perm(argv[1], 0, n-1);
    printf("count=%d",cnt);
    return 0;
}
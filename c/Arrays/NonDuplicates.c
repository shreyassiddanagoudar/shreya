#include<stdio.h>
int isRepeating(int n,int a[],int size,int index){ //n=length
            int res=0;
            for (int i=0; i<size; i++) {
                if(i!=index){
                   if(a[i]==n) {
                      res=1;
                      break;
                }
                }
            }
            return res;
}
int main(int argc,char*argv[]) {
    // if the no. is repeated in array
    int ar[5] = {1, 2, 5,5,3};
    int nr[5];
 
    int n, res, nrCnt=0;
    for(int i=0;i<5;i++){
      if(isRepeating(ar[i],ar, 5, i)==0) {
        nr[nrCnt] = ar[i];
        nrCnt++;

       
    }
    }
    for(int i=0;i<nrCnt;i++){
        printf("%d",nr[i]);
    }
return res;
}
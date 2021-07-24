#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void alagramSort(char a[], int size) {
	for (int i = 0; i<6;i++) {
		int min_idx = i;
		for (int j = i+1; j < 6;j++) {
			if (a[j] < a[min_idx])
				min_idx = j;
		}
		// swap min_idx and i element
		char temp = a[min_idx];
		a[min_idx] = a[i];
		a[i] = temp;
	}
}
int isAlagram(char str1[], char str2[]) {
    if (strlen(str1) != strlen(str2) ){
        return 1;
    }
        
    alagramSort(str1, strlen(str1));
    alagramSort(str2, strlen(str2));
    if(strcmp(str1,str1) == 0) {
        return 0;
        }     
    return 1;
}

int main() {
    char str1[]="AAABBC";
    char str2[]= "ABCAAB";
    int a = isAlagram(str1, str2);
    if(a == 0) {
        printf("is anagram");
    } else {
        printf("is not anagram");

    }
    


    
}
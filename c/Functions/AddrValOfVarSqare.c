#include <stdio.h>
int square(int a) {
	a = a * a ;
	printf("address of variable a in function is %p and its value is %d\n", &a,a) ;
	return a ;
}
int main(int argc, char *argv[]) {
	int a = 10;
	printf("address of variable a in main program is %p \n", &a) ;
	int b = square(a);
	printf("a is %d and square the value is %d \n", a, b);
	return 1;
}

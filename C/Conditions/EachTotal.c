#include <stdio.h>

int main(int argc, char*argv[]) {
    int a,b,c,d,e;
    float total, div, per;
    printf("Enter the name, rollnumber and marks\n");
    scanf("%s %d %d %d %d", &a, &b, &c, &d, &e);
    total = c+d+e;
    div =total/300;
    per =div/100;
    printf("The total %f", total);
    printf("The div %f", div);
    printf("The per %f", per);

}
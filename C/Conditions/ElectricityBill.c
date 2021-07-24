#include <stdio.h>

int main(int argc, char*argv[]) {

int unit, id;
float charge;
char name[10];
printf("Enter the unit id and name\n");
scanf("%d %d %s", &unit, &id, &name);
if(unit<=199)
{
    charge =unit*1.20;
}
else if(unit>=200 && unit<400)
{
    charge =unit*1.50;
}
else if(unit>=400 && unit<600)
{
    charge =unit*1.80;
}
else 
{
    charge =unit*2.00;
}
if (charge>400){
    charge = charge + 0.15*charge;
    printf("Electricity bill = %f", charge);
}
else if (charge<100){
    charge = 100;
    printf("Electricity bill = %f", charge);
}
else
{
    printf("Electricity bill = %f", charge);
}
}



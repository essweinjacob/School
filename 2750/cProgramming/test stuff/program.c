#include <stdio.h>
void main(){
    char name[10];
    int age;
    float gpa;

    printf("Enter your name: ");
    scanf("%s", name);
    printf("Enter your age: ");
    scanf("%d", &age);
    printf("Enter your gpa: ");
    scanf("%f", &gpa);

    printf("\nYour name is %s", name);
    printf(" Your age is %d", age);
    printf(" Your gpa is %f", gpa);
    printf("\n");
}

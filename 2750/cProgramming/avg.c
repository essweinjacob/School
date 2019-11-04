#include <stdio.h>

void main(){
    float x, y, avg;
    printf("Input 2 floating-point numbers: ");
    scanf( "%f%f", &x,&y );
    avg = average( x, y );
    printf("The average is: %f\n", avg );
}

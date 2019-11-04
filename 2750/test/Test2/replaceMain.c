#include <stdio.h>
#include <string.h>
#include "replace.c"

void main(){
    char a[6];
    scanf("Enter a string: %s\n", a);

    char *b;
    b = replace(a);

    printf("The replaced string is: %s\n", b);
}

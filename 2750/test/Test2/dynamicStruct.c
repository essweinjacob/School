#include <stdio.h>
#include <stdlib.h>

struct Edata {
    int numSize;
    char num[100];
};

void main() {
    struct Edata *ptr;

    ptr = calloc(5, sizeof(struct Edata));
    
    free(ptr);
}

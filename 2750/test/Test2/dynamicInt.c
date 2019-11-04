#include <stdio.h>
#include <stdlib.h>

void main(){
    int *space;

    space = (int *)malloc(sizeof(int)*7);

    for(int i = 0; i < 7; i++){
        space[i] = 7;
    }

    free(space);

}

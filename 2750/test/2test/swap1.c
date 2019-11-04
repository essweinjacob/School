#include <stdio.h>

int swap(int*x,int*y);

void main(){
    int x;
    int y;

    scanf("%d\n", &x);
    scanf("%d\n", &y);

    swap(&x,&y);
}

int swap(int*x,int*y){
    int t;
    t = *x;
    *x = *y;
    *y = t;

    printf("%d%d", *x,*y);

    return *x, *y;
}

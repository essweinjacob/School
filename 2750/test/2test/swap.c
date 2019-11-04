#include <stdio.h>

int *swap(int*x, int*y);

void main(){
    int x;
    int y;
    printf("Enter a #");
    scanf("%d\n",&x);
    printf("1");
//    swap(x,y);
}

int *swap(int*x, int*y){
    printf("2");
    int t;
    t=*x;
    *x=*y;
    *y=t;

    printf("%d,%d\n", *x,*y);
}

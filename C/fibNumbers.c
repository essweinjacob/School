#include <stdio.h>

int main(){
    int userNum;

    printf("How many digits of the fibonacci sequence would you like to compute?  ");
    scanf("%d", &userNum);

    printf("Fib digits of %d is %d", userNum, fibRecur(userNum));
    printf("\n");
    return 0;
}

int fibRecur(int x){
    if(x <= 1){
        return x;
    }
    return fibRecur(x-1) + fibRecur(x-2);
}
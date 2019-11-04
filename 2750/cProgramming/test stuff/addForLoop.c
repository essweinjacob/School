#include <stdio.h>

void main(){
    int sum = 0;
    int input;
    int i = 0;
    for(; i < 3; i++){
        scanf("%d", &input);
        sum += input;
    }
    printf("%d", sum);
}

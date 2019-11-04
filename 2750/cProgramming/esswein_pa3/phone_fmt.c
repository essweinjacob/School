#include <stdio.h>

void phone_fmt(char *number){
    char newNumber[14];
    int numberPos = 0;

    newNumber[0] = '(';
    for(int i = 1; i <= 3; i++){
        newNumber[i] = number[numberPos];
        numberPos++;
    }
    
    newNumber[4] = ')';
    for(int i = 5; i <= 7; i++){
        newNumber[i] =number[numberPos];
        numberPos++;
    }

    newNumber[8] = '-';
    for(int i = 9; i <= 13; i++){
        newNumber[i] = number[numberPos];
        numberPos++;
    }

    printf("New Format: %s\n", newNumber);
}

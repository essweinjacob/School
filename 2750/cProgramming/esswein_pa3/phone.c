#include <stdio.h>
#include <ctype.h>
#include "phone_fmt.h"

int main(){
    char input[200];
    char tenDigits[11];

    printf("Enter a phone number: ");
    scanf("%s", input);

    int digitCount = 0;
    int firstDigits = 0;
    for(int i = 0; i <= 200; i++){
        if(isdigit(input[i])){
            tenDigits[firstDigits] = input[i];
            digitCount++;
            firstDigits++;
        }
    }

    if(digitCount >= 10){

        printf("Ten Digits: %s\n", tenDigits);
        phone_fmt(tenDigits);

        return 0;
    }
    else{
        printf("Not enought digits entered");
        return 0;
    }
}

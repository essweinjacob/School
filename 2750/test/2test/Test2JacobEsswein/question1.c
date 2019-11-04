#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void main(){
    char string[100] = "we are going to the party";
    int numSpaces = 1;
    for(int i = 0; i <= strlen(string); i++){
        if(isspace(string[i])){
            numSpaces++;
        }
    }
    char * reverse;
    reverse = calloc(numSpaces, sizeof(char));

    for(int i = 0; i <= numSpaces; i++){
        for(int x = 0; x <= strlen(string); x++){
            reverse[i] += string[x];
            if(isspace(string[x])){
                i++;
            }
        }
    }

    for(int i = 0; i < numSpaces; i++){
        printf("%s", reverse);
    }

    printf("%s\n", string);
}

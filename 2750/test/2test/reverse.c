#include <stdio.h>
#include <string.h>

char * replace(char * str){
    for(int i = 0; i <= strlen(str); i++){
        if(isupper(str[i])){
            str[i] = tolower(str[i]);
        }
    }

    return str;
}

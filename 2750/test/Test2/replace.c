#include <stdio.h>
#include <string.h>

char *  replace(char *a){
    for(int i = 0; i <= strlen(a);i++){
        if (a[i] == 'a'){
            a[i] = 'b';
        }
    }


    return a;
}

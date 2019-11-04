#include <stdio.h>
#include <string.h>

void main(int argc, char ** argv){
    if(strlen(argv[1]) > strlen(argv[2])){
        printf("%s", argv[1]);
    }
    else{
        printf("%s", argv[2]);
    }
}

#include <stdio.h>
#include <stdlib.h>

int main(){
    char * buf;
    buf = "Hello";
    buf = "World!";
    char arr[] = "First";
    buf=arr;
    printf("%s", buf);
    printf("%s", arr);


    return 0;
}

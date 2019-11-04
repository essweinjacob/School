#include <stdio.h>

int main()
{
    int a=0;
    int ar[5];

    for(a=5;a>=0;a--){
        ar[a]=a*a;
    }
    for(a=0;a<=5;a++){
        printf("value of %d script is = %d", a, ar[a]);
        printf("\n");
    }
    
    return 0;
}

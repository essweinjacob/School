#include <stdio.h>

void main(){
    FILE *fp;
    char filename[100];

    printf("Enter file name: ");
    scanf("%s\n", filename);

    fp = fopen(filename, "w");
    fprintf(fp, "%s", "Hello this is dog");

    fclose(fp);
}

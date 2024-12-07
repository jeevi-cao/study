#include <stdio.h>
#include <stdlib.h>

#define N 100

int main() {
    FILE *fp; 
    char str[N + 1];

    if ((fp = fopen("./1.txt", "rb")) == NULL) {
        puts("Fail to open file");
        exit(0);
    }

     //循环读取文件的每一行数据
    while( fgets(str, N, fp) != NULL ) {
        printf("%s", str);
    }
   
    //操作结束后关闭文件
    fclose(fp);

    return 0;
}
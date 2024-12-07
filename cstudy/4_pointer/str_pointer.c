#include <stdio.h>
#include <string.h>

int main() {
    // char str[] = "http://c.biancheng.net";
    // int len = strlen(str), i;
    
    // printf("%s\n", str);
    // for(int i = 0; i < len; i++) {
    //     printf("%c", str[i]);
    // }

    // printf("\n");
    // for (int i = 0; i < len; i++) {
    //     printf("%c", *(str + i));
    // }
    // printf("len=%d sizeof=%ld\n", len, sizeof(str));

    // char *str1 = "http://c.biancheng.net";
    // int len2 = strlen(str1);
    // printf("len=%d sizeof=%ld\n", len2, sizeof(str1));

    char *str = "Hello World!";
    str = "I love C!";  //正确 

    char str2[20];
    printf("%s11\n", str2);

    char str1[20] = {0};
    printf("%s12\n", str1);

    return 0;
}
#include <stdio.h>
#include <string.h>
int main(){
    char str1[] = "http://c.biancheng.net";
    char str2[] = "http://www.baidu.com";
    //比较两个字符串大小
    int result = strcmp(str1, str2);
    printf("str1  - str2 = %d\n", result);
    return 0;
}
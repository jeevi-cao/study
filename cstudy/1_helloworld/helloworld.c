#include <stdio.h>
#include <string.h>
#include <wchar.h>

int main() 
{
    puts("hello world!\n");
    long abc = 123;
    unsigned long abc_len = sizeof abc;
    printf("sizeof int:%ld\n", abc_len);
    printf("%ld\n", abc);

    float c = 12.84;
    printf("%g\n", c);
    float a = 0.00001;
    printf("%g\n",a);

    char *src = "Hello, World!";  
    printf("%ld\n", strlen(src));

    // wchar_t a = L'A';  //英文字符（基本拉丁字符）
    // wchar_t b = L'9';  //英文数字（阿拉伯数字）
    // wchar_t c = L'中';  //中文汉字
    // wchar_t d = L'国';  //中文汉字
    // wchar_t e = L'。';  //中文标点
    // wchar_t f = L'ヅ';  //日文片假名
    // wchar_t g = L'♥';  //特殊符号
    // wchar_t h = L'༄';  //藏文

    puts("中华人名共和国");

    return 0;
}
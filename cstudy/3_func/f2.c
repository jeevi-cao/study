#include <stdio.h>
#include <string.h>
//反转（逆置）字符串
char *reverse(char *str) {
    int len = strlen(str);
    if (len > 1) {
        char ctemp = str[0];
        str[0] = str[len - 1];
        str[len - 1] = '\0';  //最后一个字符在下次递归时不再处理
        printf("%p\n", str+1);
        reverse(str + 1);  //递归调用
        str[len - 1] = ctemp;
    }
    return str;
}
int main() {
    char str[20] = "123456789";
    printf("%s\n", reverse(str));
    return 0;
}
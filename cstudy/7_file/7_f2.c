#include <stdio.h>
#include <stdlib.h>


int main() {
    // 定义一个文件指针fp，用于后续打开文件操作
    FILE *fp;
    // 定义一个字符变量ch，用于读取文件中的字符
    char ch;

    // 尝试以读写模式打开文件"./1.txt"，如果失败则输出错误信息并退出程序
    if ((fp = fopen("./1.txt", "r+")) == NULL) {
        puts("Fail to open file!");
        exit(0);
    }

    // 检查文件读取是否出错，如果出错则输出错误信息，否则输出成功信息
    if (ferror(fp)) {
        puts("读取出错");
    } else {
        puts("读取成功");
    }

    // 检查是否已读到文件末尾，如果已读到则输出成功信息，否则输出失败信息
    if (feof(fp)) {
        puts("feof读取成功");
    } else {
        puts("feof读取失败");
    }

    // 输出一个换行符，用于分隔不同的输出内容
    putchar('\n');

    // 将文件指针重新定位到文件开头
    rewind(fp);
    // 再次检查是否已读到文件末尾，如果已读到则输出成功信息，否则输出失败信息
    if (feof(fp)) {
        puts("feof读取成功");
    } else {
        puts("feof读取失败");
    }

    // 将字符'b'写入文件中，如果写入失败则输出错误信息
    char ch1 = 'b';
    if (fputc(ch1, fp) == EOF) {
        puts("fputc error");
    }

    // 关闭文件
    fclose(fp);

    // 程序正常退出
    return EXIT_SUCCESS;
}
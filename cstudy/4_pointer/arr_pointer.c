#include <stdio.h>

int main() {
    int arr[] = { 99, 15, 100, 888, 252 };
    int i, *p = arr, len = sizeof(arr) / sizeof(int);
    for(i=0; i<len; i++){
        printf("%d  ", *(p+i) );
    }
    printf("\n");

    int a[3][3]={1, 2, 3, 4, 5, 6, 7, 8, 9};
    printf("long arr length:%ld\n", sizeof(a));
    
    int a2[] = {1, 2, 3, 4, 5};

    printf("a2=%d\n", *(a2 + 2));


    int a = 16, b = 932, c = 100;
    //定义一个指针数组
    int *arr[3] = {&a, &b, &c};//也可以不指定长度，直接写作 int *arr[]
    //定义一个指向指针数组的指针
    int **parr = arr;
    printf("%d, %d, %d\n", *arr[0], *arr[1], *arr[2]);
    printf("%d, %d, %d\n", **(parr+0), **(parr+1), **(parr+2));
    

    return 0;
}
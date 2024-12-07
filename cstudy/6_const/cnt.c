#include <stdio.h>


int getNum() {
    return 100;
}


int main() {
    int n = 90;
    const int MaxNum1 = getNum();
    const int MaxNum2 = n;
    const int MaxNum3 = 80;
    printf("%d %d %d\n", MaxNum1, MaxNum2, MaxNum3);

    int m = 91;
    const int *p = &n;
    printf("p=%d\n", *p);
    p = &m;
    printf("p=%d\n", *p);

    int *const pp = &m;
    printf("pp=%d\n",  *pp);
    *pp = 33;
    printf("pp=%d \n", *pp);


    return 0;
}
#include <stdio.h>

int main(){
    struct stu{
        char *name;  // 姓名
        int num;     // 学号
        int age;     // 年龄
        char group;  // 所在学习小组
        float score; // 成绩
    } stu1, stu2;

    printf("struct %ld\n", sizeof stu1);
    printf("struct field size: char = %ld int %ld %ld %ld, %ld\n", sizeof(stu1.name), sizeof(stu1.num), sizeof(stu1.age), sizeof(stu1.group), sizeof(stu1.score));

    struct stu class[] = {
        {"Li ping", 5, 18, 'C', 145.0},
        {"Zhang ping", 4, 19, 'A', 130.5},
        {"He fang", 1, 18, 'A', 148.5},
        {"Cheng ling", 2, 17, 'F', 139.0},
        {"Wang ming", 3, 17, 'B', 144.5}
    };

    int i, num_140 = 0;
    float sum = 0;
    for(i=0; i<5; i++){
        sum += class[i].score;
        if(class[i].score < 140) num_140++;
    }
    printf("sum=%.2f\naverage=%.2f\nnum_140=%d\n", sum, sum/5, num_140);


    struct{
        char *name;  //姓名
        int num;  //学号
        int age;  //年龄
        char group;  //所在小组
        float score;  //成绩
    } stu3 = { "Tom", 12, 18, 'A', 136.5 }, stu4 = { "Tom", 12, 18, 'A', 136.5 };

    printf("stu3.name=%s\n", stu3.name);
    printf("stu4.name=%s\n", stu4.name);
    
    return 0;
}
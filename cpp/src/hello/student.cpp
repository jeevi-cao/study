#include <stdio.h>

class Student{
    public:
        char *name;
        int age;
        float score;
        void say(){
            printf("I am %s, %d years old, %.2f score\n", name, age, score);
        }
};


int main(){
    class Student s;
    s.name = "Tom";
    s.age = 18;
    s.score = 90.5;
    s.say();
    return 0;
}
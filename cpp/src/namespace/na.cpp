#include <string>
#include <iostream>
using namespace std;

namespace Cao
{
    class Student
    {
    public:
        int id;
        std::string name;
        int age;
        int score;
        Student(int id, std::string name, int age, int score)
        {
            this->id = id;
            this->name = name;
            this->age = age;
            this->score = score;
        }
    };
}

int main()
{
    Cao::Student s1(1, "张三", 18, 100);
    std::cout << s1.name << endl;
    std::cout << s1.age << endl;
    std::cout << s1.score << endl;

    return 0;
}
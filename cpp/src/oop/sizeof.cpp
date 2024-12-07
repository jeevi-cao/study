
#include <iostream>
using namespace std;
class Student
{
private:
    char *m_name;
    int m_age;
    float m_score;

public:
    void setname(char *name);
    void setage(int age);
    void setscore(float score);
    void show();
};

void Student::setname(char *name)
{
    m_name = name;
}

void Student::setage(int age)
{
    m_age = age;
}

void Student::setscore(float score)
{
    m_score = score;
}

void Student::show()
{
    cout << "name:" << m_name << endl;
    cout << "age:" << m_age << endl;
    cout << "score:" << m_score << endl;
}

int main()
{
    Student s;
    char name[20];
    cout << sizeof(s) << endl;
    // 在堆上创建对象
    Student *pstu = new Student();
    cout << sizeof(*pstu) << endl;
    // 类的大小
    cout << sizeof(Student) << endl;
    return 0;
}
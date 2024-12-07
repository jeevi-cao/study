/*
 * @Author: jeevi 542561541@qq.com
 * @Date: 2024-07-29 21:26:56
 * @LastEditors: jeevi 542561541@qq.com
 * @LastEditTime: 2024-07-29 21:27:24
 * @FilePath: /cpp/oop/deconstror.cpp
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
#include <iostream>
#include <string>
using namespace std;

class Demo
{
public:
    Demo(string s);
    ~Demo();

private:
    string m_s;
};
Demo::Demo(string s) : m_s(s) {}
Demo::~Demo() { cout << m_s << endl; }

void func()
{
    // 局部对象
    Demo obj1("1");
}

// 全局对象
Demo obj2("2");

int main()
{
    // 局部对象
    Demo obj3("3");
    // new创建的对象
    Demo *pobj4 = new Demo("4");
    func();
    cout << "main" << endl;

    // delete pobj4;

    return 0;
}
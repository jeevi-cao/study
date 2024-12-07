/*
 * @Author: jeevi 542561541@qq.com
 * @Date: 2024-07-29 20:49:08
 * @LastEditors: jeevi 542561541@qq.com
 * @LastEditTime: 2024-11-18 20:40:10
 * @FilePath: /cpp/oop/constructor_args.cpp
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
#include <iostream>
using namespace std;
class Demo
{
private:
    int m_a;
    int m_b;

public:
    Demo(int a);
    void show();
};

Demo::Demo(int b) : m_b(b), m_a(m_b)
{
}

void Demo::show()
{
    cout << "m_a = " << m_a << endl;
    cout << "m_b = " << m_b << endl;
}

int main()
{
    Demo d(10);
    d.show();
    return 0;
}

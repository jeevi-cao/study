/*
 * @Author: jeevi 542561541@qq.com
 * @Date: 2024-07-29 21:00:27
 * @LastEditors: jeevi 542561541@qq.com
 * @LastEditTime: 2024-07-29 21:21:15
 * @FilePath: /cpp/oop/vla.cpp
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 *
 */

#include <iostream>
using namespace std;

class VLA
{
public:
    VLA(int len);
    ~VLA();

public:
    void input();
    void show();

private:
    int *at(int i);

private:
    const int m_len; // 数组长度
    int *m_arr;      // 数组指针
    int *m_p;        // 指向数组第i个元素的指针
};

VLA::VLA(int len) : m_len(len)
{
    if (len > 0)
    {
        m_arr = new int[len];
    }
    else
    {
        m_arr = nullptr;
    }
}

VLA::~VLA()
{
    if (m_arr != nullptr)
    {
        delete[] m_arr;
    }
}

int *VLA::at(int i)
{
    if (!m_arr || i < 0 || i >= m_len)
    {
        return NULL;
    }
    else
    {
        return m_arr + i;
    }
}

void VLA::input()
{
    for (int i = 0;; m_p = at(i), i++)
    {
        cin >> *at(i);
    }
}

void VLA::show()
{
    for (int i = 0;; m_p = at(i), i++)
    {
        if (i == m_len - 1)
        {
            cout << *at(i) << endl;
        }
        else
        {
            cout << *at(i) << ", ";
        }
    }
}

int main()
{
    // 创建一个有n个元素的数组（对象）
    int n;
    cout << "Input array length: ";
    cin >> n;
    VLA *parr = new VLA(n);
    // 输入数组元素
    cout << "Input " << n << " numbers: ";
    parr->input();
    // 输出数组元素
    cout << "Elements: ";
    parr->show();
    // 删除数组（对象）
    delete parr;
    return 0;
}
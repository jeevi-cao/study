/*
 * @Author: jeevi 542561541@qq.com
 * @Date: 2024-07-30 21:09:55
 * @LastEditors: jeevi 542561541@qq.com
 * @LastEditTime: 2024-07-30 21:32:50
 * @FilePath: /cpp/src/oop/object_array.cpp
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
#include <iostream>
using namespace std;

class CSample
{
public:
    CSample()
    { // 构造函数 1
        cout << "Constructor 1 Called" << endl;
    }
    CSample(int n)
    { // 构造函数 2
        cout << "Constructor 2 Called" << endl;
    }
};

int main()
{
    cout << "stepl" << endl;
    CSample arrayl[2];

    cout << "step2" << endl;
    CSample array2[2] = {4, 5};

    cout << "step3" << endl;
    CSample array3[2] = {3};

    cout << "step4" << endl;
    CSample *array4 = new CSample[2];

    delete[] array4;

    int age;

    cout << age << endl;

    return 0;
}
/*
 * @Author: jeevi 542561541@qq.com
 * @Date: 2024-07-30 20:31:30
 * @LastEditors: jeevi 542561541@qq.com
 * @LastEditTime: 2024-07-30 20:33:45
 * @FilePath: /cpp/oop/deconstructor_init.cpp
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
#include <iostream>
using namespace std;

// 轮胎类
class Tyre
{
public:
    Tyre(int radius, int width);
    void show() const;

private:
    int m_radius; // 半径
    int m_width;  // 宽度
};
Tyre::Tyre(int radius, int width) : m_radius(radius), m_width(width) {}
void Tyre::show() const
{
    cout << "轮毂半径：" << this->m_radius << "吋" << endl;
    cout << "轮胎宽度：" << this->m_width << "mm" << endl;
}

// 引擎类
class Engine
{
public:
    Engine(float displacement = 2.0);
    void show() const;

private:
    float m_displacement;
};
Engine::Engine(float displacement) : m_displacement(displacement) {}
void Engine::show() const
{
    cout << "排量：" << this->m_displacement << "L" << endl;
}

// 汽车类
class Car
{
public:
    Car(int price, int radius, int width);
    void show() const;

private:
    int m_price; // 价格
    Tyre m_tyre;
    Engine m_engine;
};
Car::Car(int price, int radius, int width) : m_price(price), m_tyre(radius, width) /*指明m_tyre对象的初始化方式*/ {};
void Car::show() const
{
    cout << "价格：" << this->m_price << "￥" << endl;
    this->m_tyre.show();
    this->m_engine.show();
}

int main()
{
    Car car(200000, 19, 245);
    car.show();
    return 0;
}
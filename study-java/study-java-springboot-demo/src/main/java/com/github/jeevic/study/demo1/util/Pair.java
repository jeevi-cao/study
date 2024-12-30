package com.github.jeevic.study.demo1.util;

/**
 * @className: org.jeevi.demo1.util -> Pair
 * @description:
 * @author: jeevi
 * @createDate: 2023/10/24 19:46
 * @version: 1.0
 */
class Pair<T> {
    private T first;
    private T last;

    public Pair(T first, T last) {
        this.first = first;
        this.last = last;
    }

    public T getFirst() {
        return first;
    }
    public T getLast() {
        return last;
    }
    public void setFirst(T first) {
        this.first = first;
    }
    public void setLast(T last) {
        this.last = last;
    }
}

class Person implements Cloneable {
    public String name;
    public Integer age;


    public Person(String s1, Integer a1) {
        name = s1;
        age = a1;
    }


    @Override
    public Object clone()throws CloneNotSupportedException{
        return super.clone();
    }
}

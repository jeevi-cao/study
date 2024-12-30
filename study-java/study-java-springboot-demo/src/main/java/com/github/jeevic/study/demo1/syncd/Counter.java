package com.github.jeevic.study.demo1.syncd;

/**
 * @className: org.jeevi.demo1 -> Counter
 * @description:
 * @author: jeevi
 * @createDate: 2023/10/17 20:13
 * @version: 1.0
 */
public class Counter {
    private int count = 0;

    public void add(int n) {
        synchronized(this) {
            count += n;
        }
    }

    public void dec(int n) {
        synchronized(this) {
            count -= n;
        }
    }

    public int get() {
        return count;
    }
}

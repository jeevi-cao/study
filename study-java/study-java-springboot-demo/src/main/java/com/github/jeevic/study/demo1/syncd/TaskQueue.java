package com.github.jeevic.study.demo1.syncd;

import java.util.LinkedList;
import java.util.Queue;

/**
 * @className: org.jeevi.demo1.syncd -> TaskQueue
 * @description:
 * @author: jeevi
 * @createDate: 2023/10/17 20:28
 * @version: 1.0
 */
public class TaskQueue {
    Queue<String> queue = new LinkedList<>();

    public synchronized void addTask(String s) {
        this.queue.add(s);
        this.notify();
    }

    public synchronized String getTask() throws InterruptedException {
        while (queue.isEmpty()) {
            this.wait();
        }
        return queue.remove();
    }
}

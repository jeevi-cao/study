package com.github.jeevic.study.demo1.util;

/**
 * @className: PACKAGE_NAME -> Demo
 * @description:
 * @author: jeevi
 * @createDate: 2023/6/18 17:53
 * @version: 1.0
 */
public class DeadLockSample extends Thread {
    private final String first;
    private final String second;
    public DeadLockSample(String name, String first, String second) {
        super(name);
        this.first = first;
        this.second = second;
    }

    @Override
    public  void run() {
        System.out.println("first hashCode" + first.hashCode());
        System.out.println("second hashCode" + second.hashCode());
        synchronized (first) {
            System.out.println(this.getName() + " obtained: " + first);
            try {
                Thread.sleep(1000L);
                synchronized (second) {
                    System.out.println(this.getName() + " obtained: " + second);
                }
            } catch (InterruptedException e) {
                // Do nothing
            }
        }
    }
    public static void main(String[] args) throws InterruptedException {
        String lockA = "lockA" ;
        String lockB = "lockB";
        System.out.println("first hashCode" + lockA.hashCode());
        System.out.println("second hashCode" + lockB.hashCode());
        DeadLockSample t1 = new DeadLockSample("Thread1", lockA, lockB);
        DeadLockSample t2 = new DeadLockSample("Thread2", lockB, lockA);
        System.out.println(t1);
        System.out.println(t2);
        t1.start();
        t2.start();
        t1.join();
        t2.join();
    }
}

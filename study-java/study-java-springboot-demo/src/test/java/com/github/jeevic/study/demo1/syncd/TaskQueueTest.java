package com.github.jeevic.study.demo1.syncd;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

/**
 * @className: org.jeevi.demo1.syncd -> TaskQueueTest
 * @description:
 * @author: jeevi
 * @createDate: 2023/10/24 19:57
 * @version: 1.0
 */
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.MOCK)
class TaskQueueTest {

    @Test
    void counter() {
        Counter c1 = new Counter();
        Counter c2 = new Counter();

        new Thread(() -> {c1.add(1);}).start();
        new Thread(() -> {c1.dec(1);}).start();

        new Thread(() -> {c2.add(1);}).start();
        new Thread(() -> {c2.dec(1);}).start();
    }
}

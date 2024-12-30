package com.github.jeevic.study.demo1.util;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;
import java.sql.Connection;
import java.util.concurrent.TimeUnit;

/**
 * @className: PACKAGE_NAME -> org.jeevi.demo1.util.ConnectionDriver
 * @description:
 * @author: jeevi
 * @createDate: 2023/8/19 17:37
 * @version: 1.0
 */
public class ConnectionDriver {
    static class ConnectionHandler implements InvocationHandler {
        @Override
        public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
            if (method.getName().equals("commit")) {
                TimeUnit.MILLISECONDS.sleep(100);
            }
            return null;
        }
    }

    public static Connection createConnection() {
        return (Connection) Proxy.newProxyInstance(
                ConnectionDriver.class.getClassLoader(),
                new Class<?>[] {Connection.class},
                new ConnectionHandler()
        );
    }


}

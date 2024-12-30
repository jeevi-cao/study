package com.jeevi.www.service;

import com.jeevi.www.properties.HelloProperties;
import org.springframework.beans.factory.annotation.Autowired;

/**
 * @author jeevi
 */
public class HelloService {
    @Autowired
    HelloProperties helloProperties;

    public String sayHello(String userName) {
        return helloProperties.getPrefix() + userName + helloProperties.getSuffix();
    }

}

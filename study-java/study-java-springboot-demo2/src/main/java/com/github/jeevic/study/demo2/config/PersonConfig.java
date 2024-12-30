package com.github.jeevic.study.demo2.config;

import com.github.jeevic.study.demo2.service.PersonService;
import com.github.jeevic.study.demo2.service.impl.PersonServiceImpl;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @author jeevi
 */
@Configuration
public class PersonConfig {


    @Bean
    public PersonService personService() {
        System.out.println("在容器中添加了一个组件:peronService");
        return new PersonServiceImpl();
    }
}

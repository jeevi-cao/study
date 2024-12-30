package com.github.jeevic.study.demo2.service.impl;

import com.github.jeevic.study.demo2.bean.Person;
import com.github.jeevic.study.demo2.service.PersonService;
import org.springframework.beans.factory.annotation.Autowired;

/**
 * @author jeevi
 */
public class PersonServiceImpl implements PersonService {

    @Autowired
    private Person person;

    @Override
    public Person getPersonInfo() {
        return person;
    }
}

package com.github.jeevic.study.demo1.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.Comparator;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;


@Controller
class HelloWorldController {
    @ResponseBody
    @RequestMapping("/hello")
    public String hello() throws CloneNotSupportedException {
        return "Hello World!";
    }
}




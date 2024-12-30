package com.github.jeevic.study.demo2.controller;

import com.github.jeevic.study.demo2.bean.Db;
import com.github.jeevic.study.demo2.bean.Person;
import com.github.jeevic.study.demo2.po.Flag;
import com.github.jeevic.study.demo2.service.FlagService;
import com.jeevi.www.service.HelloService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.io.FileInputStream;
import java.io.InputStream;
import java.util.HashMap;
import java.util.concurrent.Callable;
import java.util.concurrent.Future;
import java.util.function.Function;

/**
 * @author jeevi
 */
@RestController
@Slf4j
public class HelloWorldController {

    private Integer incr = 0;

    @Autowired
    private Db db;

    @Autowired
    private Person person;

    @Autowired
    private FlagService flagService;


    @Autowired
    private HelloService helloService;

    @RequestMapping("/hello")
    public String Hello() {
        return "hello world";
    }


    @RequestMapping("/hello2")
    public HashMap<String, Object> Hello2() {
        HashMap<String, Object> map = new HashMap<>();

        map.put("a", 11);
        map.put("b", 222);
        map.put("name", "jeevi");
        map.put("incr", ++incr);

        log.info("this is a dog");

        return map;
    }

    @RequestMapping("/hello3")
    public Db Hello3() {
        return db ;
    }


    @RequestMapping("/hello4")
    public Person Hello4() {
        return person;
    }

    @RequestMapping("/hello5")
    public Flag Hello5(@RequestParam(value = "id") Integer id) {
        return flagService.getByFlagId(id);
    }

    @RequestMapping("/hello6")
    public String Hello6() {
        return helloService.sayHello("jeevi");
    }
}

package com.github.jeevic.study.demo2.bean;

import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

@Component
@ConfigurationProperties(prefix = "db")
@Data
public class Db {
    private String env;
    private String name;
    private String host;
    private String user;
    private String passwd;
}

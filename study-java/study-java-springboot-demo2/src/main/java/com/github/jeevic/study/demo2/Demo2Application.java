package com.github.jeevic.study.demo2;


import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.io.IOException;
import java.time.LocalDate;

/**
 * 将 beans.xml 加载到项目中
 * @author jeevi
 * @ImportResource(locations = {"classpath:/beans.xml"})
 */

@SpringBootApplication
public class Demo2Application {

    public static void main(String[] args) {
        System.out.println(LocalDate.now().toString());
        System.out.println("系统默认编码：" + System.getProperty("file.encoding"));

        byte[] byteData = new byte[100];
        System.out.println("请输入英文: ");
        try {
            System.in.read(byteData);
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println("您输入的内容如下：");
        for (int i = 0; i < byteData.length; i++) {
            System.out.print((char) byteData[i]);
        }
        System.out.println(Demo2Application.class.getClassLoader().toString());
        SpringApplication.run(Demo2Application.class, args);
    }

}

package com.jeevi.www.autoconfiguration;

import com.jeevi.www.properties.HelloProperties;
import com.jeevi.www.service.HelloService;
import org.springframework.boot.autoconfigure.condition.ConditionalOnMissingBean;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @author jeevi
 * 启用 HelloProperties，并默认将它添加到容器中
 */
@Configuration
@EnableConfigurationProperties(HelloProperties.class)
public class HelloAutoConfiguration {


    @ConditionalOnMissingBean(HelloService.class)
    @Bean
    public HelloService helloService() {
        System.out.print("this is test");
        return new HelloService();
    }
}

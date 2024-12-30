package com.jeevi.www.properties;

import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.boot.context.properties.EnableConfigurationProperties;


/**
 * @author jeevi
 */
@ConfigurationProperties("com.jeevi.www.hello")
@Data
public class HelloProperties {

    private String prefix;
    private String suffix;
}

package com.github.jeevic.study.demo1.util;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import static org.junit.jupiter.api.Assertions.*;

/**
 * @className: org.jeevi.demo1.util -> PrivateIpUtilTest
 * @description:
 * @author: jeevi
 * @createDate: 2023/10/24 19:56
 * @version: 1.0
 */
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.MOCK)
class PrivateIpUtilTest {

    @Test
    void isValidIPv4() {
        String ip = "192.169.0.1";
        assert PrivateIpUtil.isValidIPv4(ip);

        ip = "192.169.0.01";
        assert PrivateIpUtil.isValidIPv4(ip);

        ip = "192.169.0";
        assert PrivateIpUtil.isValidIPv4(ip) == false;

        ip = "192.169";
        assert PrivateIpUtil.isValidIPv4(ip) == false;


        ip = "2001:0db8:85a3:0000:0000:8a2e:0370:7334";
        assert PrivateIpUtil.isValidIPv4(ip) == false;

        ip = "ip";
        assert PrivateIpUtil.isValidIPv4(ip) == false;

        ip = "192.169.0.01L";
        assert PrivateIpUtil.isValidIPv4(ip) == false;

    }

    @Test
    void isPrivateIpV4() {
        String ip = "192.168.0.1";
        assert PrivateIpUtil.isPrivateIPv4(ip);

        ip = "192.169.0.01";
        assert PrivateIpUtil.isPrivateIPv4(ip) == false;

        ip = "192.169.0";
        assert PrivateIpUtil.isPrivateIPv4(ip) == false;

        ip = "192.169";
        assert PrivateIpUtil.isPrivateIPv4(ip) == false;

        ip = "10.220.1.9";
        assert PrivateIpUtil.isPrivateIPv4(ip);

        ip = "10.220.250.160";
        assert PrivateIpUtil.isPrivateIPv4(ip);

    }
}

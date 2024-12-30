package com.github.jeevic.study.demo1.util;

import java.util.regex.Pattern;

/**
 * @className: com.qihoo.finance.dspmanage.util -> PrivateIpUtil
 * @description: 私有ip网段检测
 * @author: jeevi
 * @createDate: 2023/5/24 15:24
 * @version: 1.0
 */
public class PrivateIpUtil {


    /**
     * 私有ip网段地址
     * A类: 10.0.0.0 - 10.255.255.255 主机位数24位
     * B类: 172.16.0.0- 172.31.225.225 主机数20位
     * C类: 192.168.0.0- 192.168.255.255 主机位16位
     * @see "https://baike.baidu.com/item/%E5%86%85%E7%BD%91ip/8881186"
     * 将ip切成四部分判断
     * @param ip ip地址
     * @return true-如果是ipv4私有地址 否则返回 false
     */
    public static boolean isPrivateIPv4(String ip) {
        try {
            if (ip == null || ip.trim().isEmpty()) {
                return false;
            }
            if (!isValidIPv4(ip)) {
                return false;
            }
            String[] networkips = ip.split("\\.");
            Integer ipAddr1 = Integer.parseInt(networkips[0]);
            Integer ipAddr2 = Integer.parseInt(networkips[1]);
            Integer ipAddr3 = Integer.parseInt(networkips[2]);
            Integer ipAddr4 = Integer.parseInt(networkips[3]);

            //A类地址判断
            if (ipAddr1 == 10 && isRangeIn(ipAddr2, 0, 255) &&
                    isRangeIn(ipAddr3, 0, 255) && isRangeIn(ipAddr4, 0, 255)) {
                return true;
            }
            // B类地址判断
            if (ipAddr1 == 172 && isRangeIn(ipAddr2, 16, 31) &&
                    isRangeIn(ipAddr3, 0, 255) && isRangeIn(ipAddr4, 0, 255)) {
                return true;
            }
            //C类地址判断
            if (ipAddr1 == 192 && ipAddr2 == 168  &&
                    isRangeIn(ipAddr3, 0, 255) && isRangeIn(ipAddr4, 0, 255)) {
                return true;
            }
        }catch (Exception ignore) {
        }
        return false;
    }


    public static boolean isRangeIn(Integer a, Integer start, Integer end) {
        return a>= start && a<= end;
    }


    private static final String IPV4_REGEX = "^(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})$";
    private static final Pattern IPv4_PATTERN = Pattern.compile(IPV4_REGEX);

    /**
     * 匹配是否是ipv4格式
     * @see "https://www.cnblogs.com/fnlingnzb-learner/p/16690576.html"
     * @param ip
     * @return
     */
    public static boolean isValidIPv4(String ip) {
        return IPv4_PATTERN.matcher(ip).matches();
    }
}

package com.github.jeevic.study.demo2.po;

import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;

import java.util.Date;

/**
 * @author jeevi
 */
@Data
public class Flag {

    private Integer id;

    private String flagName;

    private String flagTitle;

    private Byte flagPoolPriority;

    private Integer flagPoolCapacity;

    private Integer flagResultCallbackMode;

    private String flagResultCallbackSetting;

    private Integer flagStatus;

    private String flagType;

    @JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss", locale = "zh", timezone = "GMT+8")
    @JsonProperty(value="created_at")
    private Date createdAt;


    @JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss", locale = "zh", timezone = "GMT+8")
    @JsonProperty(value="updated_at")
    private Date updatedAt;


}

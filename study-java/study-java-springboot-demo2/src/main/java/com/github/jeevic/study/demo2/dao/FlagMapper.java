package com.github.jeevic.study.demo2.dao;

import com.github.jeevic.study.demo2.po.Flag;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

/**
 * @author jeevi
 */
@Mapper
public interface FlagMapper {
    /**
     * 基于flagId获取 flag 信息
     * @param id
     * @return
     */
    Flag getByFlagId(@Param("id") Integer id);

}

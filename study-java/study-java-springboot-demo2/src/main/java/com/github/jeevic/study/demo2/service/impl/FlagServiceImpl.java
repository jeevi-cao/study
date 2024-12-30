package com.github.jeevic.study.demo2.service.impl;

import com.github.jeevic.study.demo2.dao.FlagMapper;
import com.github.jeevic.study.demo2.po.Flag;
import com.github.jeevic.study.demo2.service.FlagService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;


@Service
public class FlagServiceImpl implements FlagService {

    @Autowired
    private FlagMapper flagMapper;

    @Override
    public Flag getByFlagId(Integer id) {
        if (id == null || id <= 0) {
            return null;
        }
        return flagMapper.getByFlagId(id);
    }


}

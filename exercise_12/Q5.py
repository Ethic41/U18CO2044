#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-04-21 23:13:05
# @Author  : Dahir Muhammad Dahir (U18CO2044)


def first_diff(string_1, string_2):
    if string_1 == string_2:
        return -1
    
    # Note: Counting is zero based
    count = 0
    for letter in string_1:
        if string_2[count] != letter:
            return count
        
        count += 1
    
    return count
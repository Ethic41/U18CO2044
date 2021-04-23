#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-04-21 23:36:58
# @Author  : Dahir Muhammad Dahir (U18CO2044)
# @Description : something cool


from random import choice as choose

def random_int(n):
    start = 10 ** (n - 1)
    stop = 10 ** n
    
    return choose(range(start, stop))


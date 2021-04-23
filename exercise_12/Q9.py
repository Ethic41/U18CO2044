#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-04-21 23:44:41
# @Author  : Dahir Muhammad Dahir (U18CO2044)
# @Description : something cool


from math import sqrt

def factors(n):
    factors = []
    
    for i in range(1, round(sqrt(n)) + 1):
        if n % i == 0:
            factors.append(int(i))
            factors.append(int(n / i))
    
    return set(factors)


#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-04-22 00:30:49
# @Author  : Dahir Muhammad Dahir (U18CO2044)
# @Description : something cool

from math import sqrt, ceil


def primes(n=100):
    first_n_primes = [2]
    
    next = 3
    
    while len(first_n_primes) < n:
        if not has_factor(next):
            first_n_primes.append(next)
        next += 1
    
    return first_n_primes


def primes_modified(n=100, start=2):
    first_n_primes = []
    
    next = start
    
    while len(first_n_primes) < n:
        if not has_factor(next):
            first_n_primes.append(next)
        next += 1
    
    return first_n_primes


def has_factor(num: int):
    for i in range(2, round(sqrt(num)) + 1):
        if num % i == 0:
            return True
    
    return False

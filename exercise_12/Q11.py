#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-04-21 23:58:06
# @Author  : Dahir Muhammad Dahir (U18CO2044)
# @Description : something cool


def matches(string_1, string_2):
    return len(set(list(string_1)).intersection(set(list(string_2))))


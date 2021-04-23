#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-04-22 00:17:34
# @Author  : Dahir Muhammad Dahir (U18CO2044)
# @Description : something cool


def change_case(string: str):
    new_string = ""
    for letter in string:
        if letter.upper() == letter:
            new_string += letter.lower()
        else:
            new_string += letter.upper()
    
    return new_string


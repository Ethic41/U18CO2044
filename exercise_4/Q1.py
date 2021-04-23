#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-04-22 13:25:04
# @Author  : Dahir Muhammad Dahir (U18CO2044)
# @Description : something cool


def main():
    user_length_in = input("input any length in centimeters: \n")
    try:
        length = float(user_length_in)
        if length < 0:
            raise TypeError
    except:
        print("input not a valid number try again!")
    
    print(converter(f"{length} inch")) 


def converter(length_cm: float):
    return length_cm / 2.54


if __name__ == "__main__":
    main()
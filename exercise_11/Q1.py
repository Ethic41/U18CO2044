#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-04-22 16:42:38
# @Author  : Dahir Muhammad Dahir (U18CO2044)
# @Description : something cool


def main():
    inventory = {}

    while True:
        user_input = input("[#] Enter product name and prices, in space separated format (e.g Rice 25):\n[#] Type '!Done' when finished\n")

        if user_input == "!Done":
            break

        try:
            item, price = user_input.split()
            inventory[item] = price
        except:
            print("please check your input make sure it's correct...\n")
    
    while True:
        try:
            user_input = input("[#] Enter the product name you want to retrieve:\n[#] Type '!Done' when finished\n")
            if user_input == "!Done":
                break
            
            print(inventory[user_input])
            
        except:
            print("Item not in inventory")


if __name__ == "__main__":
    main()


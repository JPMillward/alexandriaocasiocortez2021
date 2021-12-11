#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 18:48:18 2021
@author: johnm
"""
import re 

path = "/Users/johnm/Documents/GitHub/alexandriaocasiocortez2021/input/"
day = "day5.txt"
f = open(path + day, 'r')
day_input = f.readlines()

class DayFive():
    
    def __init__(self, input_list):
        self.input = input_list

        self.process_input()
        return
    
    
    def process_input(self): 
        for line in self.input_list:
            print(line.strip(\n))
        return
    
   
DayFive(day_input)
#print(day4_input)f


#print(input_list)
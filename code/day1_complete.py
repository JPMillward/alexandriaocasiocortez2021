#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 00:05:21 2021

@author: johnm

#Advent of Code 2021
"""
import requests
import io

path = "/Users/johnm/Documents/GitHub/alexandriaocasiocortez2021/input/"
day = "day1.txt"
f = open(path + day, 'r')
input_file = f.readlines()
#Could either recursion out the first input or just cheat it by accounting for it in the counter.
deeper = -1
last_depth = 0
for item in input_file:
    new_depth = int(item.strip('\n'))
    #print(f"Previous Depth: {last_depth}, Current Depth: {new_depth}")
    if new_depth > last_depth: deeper += 1
    last_depth = new_depth
print(deeper)

print(len(input_file))

rolling_depth = -1
last_sum = 0
for x in range(len(input_file) -2):
    current_depth = int(input_file[x])
    next_depth = int(input_file[x+1])
    third_depth = int(input_file[x+2])
    rolling_sum = current_depth + next_depth + third_depth
    
    if rolling_sum > last_sum: rolling_depth += 1
    last_sum = rolling_sum
print(rolling_depth)

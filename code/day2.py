#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 08:48:33 2021

@author: johnm
"""
import re

path = "/Users/johnm/Documents/GitHub/alexandriaocasiocortez2021/input/"
day = "day2.txt"
f = open(path + day, 'r')
input_file = f.readlines()

aim = 0
depth = 0
distance = 0

for line in input_file:
    split = re.split(' ', line.strip('\n'))
    if split[0] == 'up':
        aim -= int(split[1])
    if split[0] == 'down':
        aim += int(split[1])
    if split[0] == 'forward':
        distance += int(split[1])
        depth += aim*int(split[1])
    print(split, aim, distance, depth)
        
print(aim)
print(depth)
print(distance)
final_dist = depth*distance
print(final_dist)
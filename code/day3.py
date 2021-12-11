#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 09:16:46 2021

@author: johnm
"""

import pandas as pd

path = "/Users/johnm/Documents/GitHub/alexandriaocasiocortez2021/input/"
day = "day3.txt"
f = open(path + day, 'r')
input_file = f.readlines()
count_dict = {'0' : {'0' : 0, '1':0},
              '1' : {'0' : 0, '1':0},
              '2': {'0' : 0, '1':0},
              '3': {'0' : 0, '1':0},
              '4': {'0' : 0, '1':0},
              '5': {'0' : 0, '1':0},
              '6': {'0' : 0, '1':0},
              '7': {'0' : 0, '1':0},
              '8': {'0' : 0, '1':0},
              '9': {'0' : 0, '1':0},
              '10': {'0' : 0, '1':0},
              '11': {'0' : 0, '1':0}}
              


for line in range(len(input_file)):
    for digit in range(len(input_file[line].strip('\n'))):
        this_digit = str(input_file[line][digit])
        #print(count_dict[str(digit)][this_digit])
        count_dict[str(digit)].update({this_digit:int(count_dict[str(digit)][this_digit])+1})

gamma_greater = ''
epsilon_lesser = ''
for key in count_dict.keys():
    digit = count_dict[key]
    if digit['0'] > digit['1']:
        gamma_greater += '0'
        epsilon_lesser += '1'
    elif digit['1'] > digit['0']:
        gamma_greater += '1'
        epsilon_lesser += '0'

gamma = int(gamma_greater, 2)
epsilon = int(epsilon_lesser, 2)

print(gamma_greater, epsilon_lesser)
print(gamma, epsilon, gamma*epsilon)

def get_common_bit(bit_list, position, by_most_common = True):
    one = 0
    zero = 0
    for bit in bit_list:
        if int(bit[position]) == 1: one += 1
        elif int(bit[position]) == 0: zero += 1
        else: return ValueError(f"Cannot Have a bit of value {bit[position]}")
    #print(by_most_common)
    #print(one, zero)
    if one > zero: 
        mcv = 1
        lcv = 0 
    elif zero > one: 
        mcv = 0
        lcv = 1
    elif zero == one:
        mcv = int(by_most_common)
        lcv = int(by_most_common)

    if by_most_common == True: return mcv        
    elif by_most_common == False: return lcv
        

def diagnostic_crawl(diagnostics_report, by_mcv, crawl = 0):
    some_common_bit = get_common_bit(diagnostics_report, position=crawl, by_most_common=by_mcv)   
    
    diagnostics_report = [item for item in diagnostics_report if int(item[crawl])==some_common_bit]
    print(len(diagnostics_report))
    if len(diagnostics_report) == 1:
        print(int(diagnostics_report[0],2))
        return
    elif len(diagnostics_report)>0:
        diagnostic_crawl(diagnostics_report, by_mcv, crawl+1)
    else:
        return print("Uhhh")


report = [line.strip() for line in input_file]
print(diagnostic_crawl(report, by_mcv = True))
print(diagnostic_crawl(report, by_mcv = False))

print(1679*3648)

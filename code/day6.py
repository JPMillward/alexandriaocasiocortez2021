#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 18:48:18 2021
@author: johnm
"""
import re 

path = "/Users/johnm/Documents/GitHub/alexandriaocasiocortez2021/input/"
day = "day6.txt"
import re
f = open(path + day, 'r')
day_input = f.readlines()

test_case = [3,4,3,1,2]

class DaySix():
    
    def __init__(self, input_list):
        self.input = input_list
        self.spawn_timer = 8
        self.birth_cycle = 6
        self.day = 0
        self.fish_pool = {fish_state : 0 for fish_state in range(9)}
        return
    
    
    def process_input(self): 
        #self.spawn_pool = [int(x) for x in self.input]
        
        spawn_list = self.input[0].strip('\n')
        spawn_pool = spawn_list.split(',')
        self.spawn_pool = [int(x) for x in spawn_pool]
        for fishy in self.spawn_pool:
            self.fish_pool[fishy] += 1
        
        return
    
    def fornicate_fish(self, days):
        
        for key, value in self.fish_pool:
            if key == 0:
                
        
        #print(self.spawn_pool)
        return
    
    def calculate_fish(self, days):
        print(self.day, days)
        while self.day < days:
            self.spawn_day_timer()
            print(self.day)
    
        return print(len(self.spawn_pool))
            
   
print(DaySix(day_input).calculate_fish(256))
#print(day4_input)f


#print(input_list)
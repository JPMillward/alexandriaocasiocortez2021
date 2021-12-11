#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 18:48:18 2021
@author: johnm
"""
import re 

path = "/Users/johnm/Documents/GitHub/alexandriaocasiocortez2021/input/"
day = "day11.txt"
f = open(path + day, 'r')
day_input = f.readlines()

class DayEleven():
    
    def __init__(self, input_list):
        self.input = input_list
        self.step_count = 0
        self.flash_count = 0
        self.flash_value = 10
        self.octopi_grid = []
        self.flash_locations = []
        
        
        self.process_input()
        print(self.octopi_grid)
        return
    
    
    def process_input(self): 
        for line in self.input:
            self.octopi_grid.append([int(x) for x in line.strip()])
        return
    
    def iterate_octopi(self):        
        for x, row in enumerate(self.octopi_grid):
            for y, column in enumerate(row):
                row[y] += 1
                if row[y] == self.flash_value:
                    self.flash_locations.append({'x':x, 'y':y})
                    self.flash_count += 1
        return
    
    def handle_flashes(self):
        #print(self.flash_locations)
        for flash in self.flash_locations:
            x = flash['x']
            y = flash['y']
            #print(f"{x},{y}")
            for x_coord in range(-1,2):
                new_x = x + x_coord
                if new_x not in [value for value in range(len(self.octopi_grid))]:
                    #print('Outside Bounds')
                    None
                else:
                    
                    for y_coord in range(-1,2):
                        new_y = y + y_coord
                        if new_y not in [value for value in range(len(self.octopi_grid[x]))]:
                           #print('outside bounds')
                           None
                        else:                            
                            self.octopi_grid[new_x][new_y] += 1
                            
                            if (self.octopi_grid[new_x][new_y]) == self.flash_value:
                                print(f" x: {new_x}, y: {new_y}")
                                self.flash_locations.append({'x':new_x, 'y':new_y})
                                self.flash_count += 1
                
        #print(self.flash_locations)
        return
    
    def handle_single_step(self):   
        self.iterate_octopi()
        self.handle_flashes()
        self.flash_locations.clear()
        
        for x,row in enumerate(self.octopi_grid):
            for y,column in enumerate(row):
                if self.octopi_grid[x][y] >= self.flash_value:
                    self.octopi_grid[x][y] = 0
        for row in self.octopi_grid:
            print(row)
        return
        
    
    def take_steps(self, step_number):
        for row in self.octopi_grid:
            print(row)
        while step_number > 0:
            self.handle_single_step()
            self.step_count += 1
            
            if self.check_synch() == True:
                return self.step_count
            step_number -= 1

        return self.flash_count
    
    def check_synch(self):
        for row in self.octopi_grid:
            print(row)
            for column in row:
                if column != 0:
                    return False
        return True
    
    
print(DayEleven(day_input).take_steps(500))

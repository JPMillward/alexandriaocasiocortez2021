#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 18:48:18 2021
@author: johnm
"""
import re 

path = "/Users/johnm/Documents/GitHub/alexandriaocasiocortez2021/input/"
day = "day4.txt"
f = open(path + day, 'r')
day4_input = f.readlines()

class DayFour():
    
    def __init__(self, input_list):
        self.input = input_list
        self.call_queue = []
        self.called_numbers = []
        self.bingo_cards = []
        self.solutions = {}
        
        self.card_wins = []
        
        self.process_input()
        self.get_valid_solutions()
        return
    
    
    def process_input(self): 
        bingo_board = []
        for line in self.input:
            if ',' in line:
                call_line = re.split(',', line.strip())
                for call in call_line:
                   self.call_queue.append(int(call))
                print(f"Bingo Calls: {self.call_queue}")
            
            elif line == '\n':
                if len(bingo_board) == 5:
                    self.bingo_cards.append(bingo_board)
                    bingo_board = []
                if len(bingo_board) > 5: return ValueError(f"Error: board has {len(bingo_board)} rows. Five is max.")
            
            else:
                board_row = re.split('\s+', line.strip())
                board_row = [int(x) for x in board_row]
                print(board_row)
                bingo_board.append(board_row)
        if len(bingo_board) == 5:
            self.bingo_cards.append(bingo_board)
        return
    
    
    def cheat_at_bingo(self):
        for card_number, winning_lists in self.solutions.items():
            print(self.called_numbers)
            print('\n')
            #for item in self.bingo_cards[card_number]:
                #print(item)
            
            for winning_numbers in winning_lists:
                print(winning_numbers)
                #print(self.called_numbers)
                check_win = []
                for item in winning_numbers:
                    if int(item) in self.called_numbers:
                        check_win.append(item)      
              
                if len(check_win) == 5:
                    #print(check_win)
                     if card_number not in self.card_wins:
                         self.card_wins.append(card_number)
       
        
        if len(self.card_wins) == len(self.bingo_cards):
            self.winning_card = self.bingo_cards[self.card_wins[-1]]
            return True
        print('\n')
        return False
        
        
    def get_valid_solutions(self):
        for entry,card in enumerate(self.bingo_cards):
            card_bingos = []
            down_right = []
            up_left = []
  
            #initalize dictionary of empty lists that has keys for each column
            column_bingos = { x : list() for x in range(len(card[0]))}
            #print(column_bingos)
            for row_number, row in enumerate(card):
                card_bingos.append(row)

                for column_number, bingo_number in enumerate(row):
                    new_column = [*column_bingos[column_number], bingo_number]
                    column_bingos.update({ column_number : new_column })
                    
                    
                    if row_number == column_number:
                        down_right.append(bingo_number)
        
                    if row_number + column_number == 4:
                        #print(row_number, column_number)
                        up_left.append(bingo_number)
                
            for key,value in column_bingos.items():
                card_bingos.append(value)
            
            #card_bingos.append(down_right)
            #card_bingos.append(up_left)
            
            print(f"Card Number {entry}, bingos: {len(card_bingos)}")
            self.solutions.update( {entry : card_bingos})      
        return

    def play_bingo(self):      
        for call_number in self.call_queue:
            print(f"Bingo Number: {call_number}")
            self.called_numbers.append(call_number)
            
            
            if self.cheat_at_bingo() == True:
                self.do_the_math(call_number)
                return 
        
        print(f"{len(self.card_wins)}, {len(self.bingo_cards)}")
        print(self.card_wins)
                
    
    def do_the_math(self, call_number):
        
        print(f"Winning Card:\n{self.winning_card[0]}\n{self.winning_card[1]}\n{self.winning_card[2]}\n{self.winning_card[3]}\n{self.winning_card[4]}")
        #print(f"Winning Line: \n{self.winning_line}, Call Number:\n {call_number}")
        print(self.called_numbers)
        card_values = []
        
        for row in self.winning_card:
            card_values = [*card_values, *row]
    
        card_values = [int(x) for x in card_values if x not in self.called_numbers]
        print(card_values)
        
        card_sum = 0
        for x in card_values:
            card_sum += x
            
        print(card_sum, int(call_number))
        print( card_sum * int(call_number) )

DayFour(day4_input).play_bingo()
#print(day4_input)


#print(input_list)
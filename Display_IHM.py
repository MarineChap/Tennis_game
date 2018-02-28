#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import libraries

import numpy as np
import sys

"""
 One way to control the user input is to use a while loop with a try/except structure. 
 If the input match with the expected format, the program continues. 
 If not, the question is asked again and again until we have the right answer. 
"""
def protect_input_integer(str):
    while True :
        try:
            value = int(input(str))
            break
        except:
            print('You have enter a wrong input')
    
    return value
    
# Initialization and mode selection

def selection_play_mode():
    
    name_player    = ['','']
    name_player[0] = input('Name of the 1st player : ')
    name_player[1] = input('Name of the 2nd player : ')
    
    nb_set = protect_input_integer('Number of winner set: ')

    while True:
        try:                
            mode = int(input('Do you want to initialize a new match or load a match in progress (1/2) ?'))
            
            if mode == 1:
                number_set = 0
                set_gagne  = [0,0]
                game       = np.zeros((2, 2*nb_set), dtype = int)
                break
            
            elif mode == 2:
                set_gagne, number_set, game = load_match(name_player, nb_set)
                break
            
        except :
            continue
        
        print('You have enter a wrong input')

    print('Let\'s go ', name_player[0], 'and', name_player[1], '!')
    
    return name_player, nb_set, set_gagne, number_set, game


#  Selection of the game's winner 
    
def select_player(name_player):

    while True:
        try:
            print('Which player won this game ? (', name_player[0],' = 1 / ',name_player[1],' = 2)')
            print('To cancel the last game, click on 0')
            winner_player = int(input('To quit the game, click on 3 :'))
            
            if winner_player >= 0  and winner_player <= 2 :
                break
        except :
            continue
        
        if winner_player  == 3 :
            print('End of the match')
            sys.exit()
            
        print('You have enter a wrong input')
        
    return winner_player 

# Load previous results to continue the match

def load_match(name_player, nb_set):
    
    set_gagne = [0,0]
    
    for j in range(2) :
        print('How many set', name_player[j], 'has been win in the previous match ?')
        set_gagne[j] = int(input())
    
    number_set = set_gagne[0] + set_gagne[1]
    game       = np.zeros((2, 2*nb_set), dtype = int)

    for i in range(number_set) :
        print('What is the score of the set', (i+1),
              '. Don\'t forget to validate between the score of ', name_player[0], 'and', name_player[1])
        game[0,i] = protect_input_integer(" ") 
        game[1,i] = protect_input_integer(" ")
    
    return(set_gagne, number_set, game)


# Display the score
    
def display_result(service, score, game, name_player, number_set) :
    
    print ('         service', end=" ")
    
    i = 0
    while (i <= number_set):
        print ('set',(i+1), end=" ")
        i = i+1
    print ('Jeu')
    print ('1.', name_player[0],'|', end=" ")
    
    if service == 0:
        print (' * |', end=" ")
    else:
        print ('   |', end=" ")
        
    i = 0
    while (i <= number_set):
        print (game[0, i],'|', end=" ")
        i = i+1
        
    print (score[0])
    print ('2.', name_player[1],'|', end=" ")
    
    if service == 1:
        print (' * |', end=" ")
    else:
        print ('   |', end=" ")
        
    i = 0
    while (i <= number_set):
        print (game[1, i], '|', end=" ")
        i = i+1
        
    print (score[1])


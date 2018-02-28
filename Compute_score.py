#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import libraries
from Display_IHM import select_player

"""
 Score dictionary : We are using a dictionary to manage the nonlinear scoring specific to the tennis. 
 The point which follows 40 is different in function of the opponent. 
 To manage this, we are adding a state "possible_game". 
 The specificity of equality is managed in the scoring function. 
"""

def score_list(x):
    return {
        '0': '15',
        '15': '30',
        '30': '40',
        '40': 'Possible_game',
        'A' : 'Game',
    }.get(x, '0')

"""
 Scoring

 To score, we are using the dictionary above. Then, we manage game equality with an if structure.
 If the player who has just won the point, had already reached 40 points at the previous game.
     Case 1 : if the opponent has the advantage, everybody comes back to 40/40
     Case 2 : if the opponent has a lowest score or the winner had already the advantage, he wins the set
     Case 3 : if both players are equal 40/40. The winner takes the advantage. 
""" 

def scoring(winner_player, score):
   
    opponent      = winner_player % 2
    winner_player = winner_player - 1
    
    score[winner_player] = score_list(score[winner_player])

    if  score[opponent] == 'A' :
        score[opponent]      = '40'
        score[winner_player] = '40'
        
    elif(score[winner_player] == 'Possible_game' and (score[opponent]!= '40' or score[winner_player] =='A')) :
        score[winner_player] = 'Game'
        
    elif(score[winner_player] == 'Possible_game' and score[opponent] == '40') :
        score[winner_player] = 'A'
    
    return (score)

"""
 Scoring game 
 
 In this function, we score the game. 
 We return the number of game win for each player and a boolean to show if the set is a win.
 Reminder : A set is won, when one player win at least 6 games with a minimum of 2 games in advance on the opponent
 But when both players are equal 6/6, we begin a new game's step called tie-break. 
"""

def scoring_game(winner_player, game, number_set) :
    
    opponent      = winner_player % 2
    winner_player = winner_player - 1
    
    game[winner_player, number_set ] = game[winner_player, number_set] + 1
    
    if   game[winner_player, number_set ] > 5  and (game[opponent, number_set] <= game[winner_player, number_set] - 2) :
        set = 'win'
    elif game[winner_player, number_set ] == 6 and  game[opponent, number_set] == 6 :
        set = 'tie_break'
    else :
        set= 'loose'
    return (game, set)

"""
 Tie Break
 
 Reminder : In case of game's equality (6-6), we begin a tie-break. 
 It is a particular time in the match. It is why we prefer to begin 
 a new cycle of loop outside of the principal function. 
 The player who has won is the first to reach 7 points with a gap of 2 points with his opponent. 
"""

def tie_break(name_player, service) :
    print ('-------- Tie-Break ---------')
    game    = [0,0]
    nb_game = 2 
    
    while True :
        
        winner_player = select_player(name_player)
        opponent      = winner_player % 2
        winner_player = winner_player - 1
        
        game[winner_player] = game[winner_player] + 1
        
        print ('     Service | Tie-break |')
        print ('1.', name_player[0], '|', end=" ")
        
        if service == 0 :
            print (' * |', end=" ")
        else :
            print ('   |', end=" ")
            
        print (game[0],  '|')
        print ('2.', name_player[1], '|', end=" ")
        
        if service == 1 :
            print (' * |', end=" ")
        else :
            print ('   |', end=" ")
            
        print (game[1], '|')
        nb_game = nb_game + 1
        
        if nb_game > 2 :
            nb_game = 1
            service = (service +1)%2
        
        if game[winner_player ] > 7 and (game[opponent] <= game[winner_player] - 2) :
            print ('--------', name_player[winner_player], 'win the set ---------')
            return winner_player


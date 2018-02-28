#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
   Tennis scoring system 
  
  This program is separated in 3 files : 
      - Score_Tennis_Game.py : Principal function
      - Display_IHM.py       : Display's function about initialization menu and selection of player winner 
      - Compute_score.py     : Computing the score and managing the current game (especially for the tie-break)
"""
# Import libraries

import random
import Display_IHM as ihm
import Compute_score as sc

# Initialization of data with a classic way or the loading of a game already begun

name_player, nb_set, set_win, number_set, game = ihm.selection_play_mode()
service = random.randint(0, 1)

# Run a match (counting the number of set fixed in the menu)
while( set_win [0] != nb_set and set_win [1] != nb_set ):
    
    # Initialization of internal variables
    set = 'loose'
    winner_player = 0

    #  Run a set : counting the number of game until someone won and managing service turns and the tie-break)
    while set == 'loose' :
        
        # Initialization of internal variables
        score = prev_score = ['0','0']
        
        #  Run a game 
        while( score[0] != 'Game' and score[1] != 'Game' ):
            
            # Ask for the winner of the game
            winner_player = ihm.select_player(name_player)
            
            # Cancel the previous game's result in case of mistake 
            if  winner_player == 0 :
                score = prev_score
                print('The last point has been cancelled')
                continue
                
            """
             A common mistake in python is to want copy a list by directly writing prev_score = score
             The problem is when we do this, we only copy a reference. 
             The object scoring is not duplicate in memory. We can check this information with the id function
             applied on each object is similar. 
             To fix this problem, we need to use the constructor of the class list which creates a reproduction 
             of the sequence given in parameters. 
             This time, prev_scoring has his own memory box and won't be modified by modification 
             on the reference of the variable scoring.
            """
        
            # Duplicate and save the previous score
            prev_score = list(score)
            
            # Update the game' score
            score = sc.scoring(winner_player, score)
            
            # Display result 
            ihm.display_result(service, score, game, name_player, number_set)
    
        # Update the set' score 
        game, set = sc.scoring_game(winner_player, game, number_set)
        
        # Manage the case of 'tie-break' 
        if set == 'tie_break':
             winner_player = sc.tie_break(name_player, (winner_player-1) )+1
        
        # Manage the service's turn
        service = (service + 1)%2
        
        print('-------- Game ---------')
    
    number_set = number_set + 1

    # Counter the number of set won by each player during the match
    set_win[winner_player -1] = set_win[winner_player -1] + 1

# Display the winner 
if set_win[0] == nb_set :
    print('Congrats', name_player[0], '!')
else :
    print('Congrats', name_player[1], '!')


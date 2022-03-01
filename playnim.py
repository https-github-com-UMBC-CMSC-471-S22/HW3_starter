""" A program to play Nim with any number of heaps that assumes we are using the aima-python
games.py framework. Usage examples:

python playnim <heaps> <player1> <player2> <heuristic>

  Runs a nim game with initial state <heaps> between <player1> and <player2> with suitable defaults

  <heaps> should be a string that will evaluate to a list of one or 
    more positive integers, e.g., [5,4,3] or [1,1,1] or "[3, 4, 5]" but not [5, 4, 3]

  <player1> and <player2> are optional and if not given default to a random player, i.e.,
    one that selects possible modes at random. Predefined player names include:

    me: for an interactive player that asks you for each move
    random: for a player that selects legal moves randomly
    mm: for a simple minimax algorithm that processes the full game tree
    ab:  for the alphabeta version that processes the full game tree

    abN, where N is an integer between 1 and 10, for a player that uses
       alphabeta and generates a lookahead tree for each move to depth N.
       Example: ab3 always looks ahead three plys.

   heuristic: should be either True of False (the default).  If True it will use a heuristic
       for computing the evaluation of a board position that is not terminal
"""

import argparse           # for calling from the command line
import games4e as games   # AIMA code
import nim                # your code

infinity = float('inf')

# PLAYERS is a dictionary mapping player names to the python functions that implement them. A player
# function takes two arguments, a game and a state.  We add to the PLAYERS dictionary player
# function named ab1,ab2,...ab10 that use alpha_beta_search with depth cutoffs between 1 and 10

PLAYERS = {'me':games.query_player,
           'random':games.random_player,
           'mm': lambda g,s: games.minmax_decision(s, g),
           'ab': lambda g,s: games.alpha_beta_search(s, g)}

for N in range(1,10):
    PLAYERS['ab'+str(N)] = lambda g, s: games.alpha_beta_cutoff_search(s, g, d=N)

# list of the names of possible players
possible_players = PLAYERS.keys()

def play_nim(heaps, player1, player2, heuristic):

    """ Play a NIM game using player1 and player2 with an initial state having the heaps heaps.
    Returns True if the play was successful and False if there was some problem, e.g., bad input or
    a draw, whuch should never happen."""

    print(f"NIM with heaps {heaps} using players {player1} and {player2} with heuristic {heuristic}" )

    # test heaps to ensure it's a list of positive integers
    if not (isinstance(heaps, list) and
            all((isinstance(item, int) and item >= 0)
                for item in heaps)):
        print(f"First argument must be a list of positive integers: {heaps}")
        return False

    # get player1 and player2 functions
    if player1 in PLAYERS:
        player1 = PLAYERS[player1]
    else:
        print(f"I don't know what kind of player {player1} is")
        print("It must be one of", possible_players)        
        return False
    
    if player2 in PLAYERS:
        player2 = PLAYERS[player2]
    else:
        print(f"I don't know what kind of player {player2} is")        
        print("It must be one of", possible_players)                
        return False

    # play the game
    game = nim.Nim(heaps=heaps, heuristic=heuristic)
    utility = game.play_game(player1, player2)

    # report the results and return True
    if utility == infinity:
        print('Player 1 wins')
        return True
    elif utility == - infinity:
        print('Player 2 wins')
        return True
    else:
        print(f'Utility = {utility}, No one wins?')
        return False
      

# if called from command line, call main with optional args for intial and goal states if provided
if __name__ == "__main__" :
  a = argparse.ArgumentParser()
  argparse.ArgumentParser(description='Play NIM given heaps and two players')
  a.add_argument('heaps', nargs="?", default = "[3,4,5]", help='Python list of initial heap sizes')
  a.add_argument('player1', nargs="?", choices = possible_players, default = 'random', help='first player')
  a.add_argument('player2', nargs="?", choices = possible_players, default = 'random', help='second player')
  a.add_argument('heuristic', nargs="?", default = False, help='use heuristic') 
  args = a.parse_args()
  play_nim(eval(args.heaps), args.player1, args.player2, heuristic=args.heuristic)

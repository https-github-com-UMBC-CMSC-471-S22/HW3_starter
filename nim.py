from collections import namedtuple
import games4e as games

infinity = float('inf')

class Nim(games.Game):

    """ Nim is a two player game where the players are identified as 1
    and 2.  Player 1 is first to move. The state of the game is a
    namedtuple with at least two attributes: to_move (the player whose
    turn it is to move) and board (a Python data structure
    representing how many heaps there are and how many objects are in
    each)."""

    def __init__(self, heaps=[1,1], show_moves=True, heuristic=False ):
        self.show_moves = show_moves
        self.heaps = heaps
        self.heuristic = heuristic
        self.initial = games.GameState(to_move=1, board=heaps, utility=0, moves=[])
        
        # check args to make sure they are legal
        if not (isinstance(heaps, list) and all(isinstance(x, int) for x in heaps)):
            raise ValueError(f"heaps mut be a list of integers")


    def actions(self, state):
        """ Given a state, return a list of legal moves. How you
        represen a move is up to you and will depend on how you
        represent the board"""

        pass

    def result(self, state,  move):
        """Given a move and a state, returns a representation of the
        new state that results after making the move."""

        pass

    def terminal_test(self, state):
        """ Returns True iff state is a terminal state, i.e., one in
        which no moves are possible."""

        pass

    def utility(self, state, player):

        """ Given a state, returns a number representing the state's
        utility with respect to the player for whom a play is being
        selected.  The state should encode who's turn it is to move.
        A simple version might return check to see if the state is
        terminal (i.e., one where all the heaps are 0) and then return
        -infinity if the the state's to_move element is the same as
        the player and + infinity otherwise.  If the game is called
        with heuristic=True, you could compute a value for
        non-terminal states; positive states that are good for the
        game's player and negative for the opponent. """

        if self.terminal_test(state):
            pass
        elif not self.heuristic:
            pass
        else:
            pass

    def __repr__(self):
        """ A simple string reprsentation of the NIM game instancew """
        return f"Nim({self.heaps})"

    def play_game(self, *players):

        """Play an n-person, move-alternating game. This a version of
        the method from the aima-python games.py program that has been
        modified to check for exacly two players and optionaly print
        moves made by each player."""

        state = self.initial
        if self.show_moves:
            print(f"Initial state: {state}")

        # let the two players alternate making moves until a terminal
        # state is reached. Return the final value, which will be plus
        # or minus infinity

        while True:
            for player_num, player in enumerate(players):
                # player_num will be 0 or 1, so add one to make them 1 or 2
                player_num += 1

                # player is one of the provided functions (e.g.,
                # random, me, mm, ab) and when called with the current
                # game state, will return a move
                move = player(self, state)

                # Your result method returns a new state by applying
                # the selected move to the current state
                state = self.result(state, move)

                # print the player, her move and resulting state
                if self.show_moves:
                    print(f"Player {player_num} moves {move} ==> {state}")

                # if it's terminal state, we return from the play_cam
                # function with the final utility value (+infinity if
                # the first player wins, -infinity if the second
                # player wins)
            
                if self.terminal_test(state):
                    return self.utility(state, self.to_move(self.initial))


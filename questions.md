# CMSC 471 Spring 2022 questions for HW3

## Name: *your name here*
## UMBC userid: *your userid here*


## 0. Answer the following questions for the Magic Squares problem

Complete the program ms.py. Be sure to run your code sending its output to ms_out.txt (20)

0.1 One way to characterize the difficulty of an NxN magic square problem is by the number of candidate solutions, where a candidate solution is some assignment of the integers between 1 and N**2 to cells in the square.  Given this measure, what is a simple upper bound on the difficulty of for N in {3,4,5,6}. (2.5)

*... your answer here ...*

0.2 The MinConflicts() solver fails to solve even the smallest magic squares problem. Review the algorithm in our text and/or examine to code in constraints.py for this solver to see why it fails to find a solution. Explain why MinConflicts() does not work well for this problem. (2.5)

*... your answer here ...*

0.3 Can you get a solution for a magic square of size six using any of the solvers and if so, how long does it take? (2.5)

*... your answer here ...*

0.4 Do you think that using CSP is a good approach for generating magic squares? Explain why or why not. (2.5)

*... your answer here ...*

## 1. Minimax and Alphabeta

1.1 For the [first game tree on the HW3 page](mm0.png), use the minimax algorithm to compute a value for each non-leaf node. Squares represent max nodes and circles represent min nodes. Indicate which move the maximizing player should make.

1.2 Simulate the alpha-beta algorithm on the [second game tree on the HW3 page](mm1.png), crossing out the nodes that are pruned. For each non-leaf node that is not pruned, show the exact value (e.g., =3) or the last constraint (e.g., <= 2, >=8) that the alpha-beta algorithm determines.


## 2. Game characteristics

For each of the following statements, say whether it is true or false and provide a short (e.g. one paragraph) justification for your answer.

2.1 Given a two-player, turn-taking, zero-sum, fully observable game between two perfectly rational players, it does not help the first player's outcome to know what strategy the second player is using -- that is, what move the second player will make, given the first player's move. (2)

*...your answer here ...*

2.2 Given a two-player, turn-taking, zero-sum, partially observable game between two perfectly rational players, it does not help the first player to know what move the second player will make, given the first player's move. (2)

*...your answer here ...*

2.3 A perfectly rational backgammon-playing agent with unlimited resources never loses. (1)

*...your answer here ...*


## 3. Answer the following questions for the game of Nim.

3.1 For a Nim game with initial configuration [5,4,3], what is the shortest possible game in terms of plys? (2.5)

*...your answer here ...*

3.2 For a Nim game with initial configuration [5,4,3], what is the longest possible game in terms of plys? (2.5)

*...your answer here ...*

3.3 For a Nim game with initial configuration [H1, H2, ... Hn] where the Hi values are all positive integers greater than 0 and n is greater than 0, what is the shortest possible game in terms of plys? (2.5)

*...your answer here ...*

3.4 For a Nim game with initial configuration [H1, H2, ... Hn] where the Hi values are all positive integers greater than 0 and n is greater than 0, what is the longest possible game in terms of plys? (2.5)

*...your answer here ...*

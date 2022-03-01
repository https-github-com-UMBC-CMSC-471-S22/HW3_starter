#! /usr/bin/python

"""
python testnim.py runs a set of test cases using the playnim.py script

"""

from playnim import play_nim

# NIM problems for testing
tests = [
    ([1], 'random', 'random',False),
    ([3], 'random', 'random',False),
    ([1,1], 'random', 'random',False),
    ([1,1], 'ab', 'ab',False),
    ([1,1,1], 'ab', 'ab',False),
    ([1,1,1,1], 'ab', 'ab',False),    
    ([2,2], 'ab', 'ab',False),
    ([1,2,3], 'ab', 'ab', False),
    ([1,2,3], 'ab', 'ab1', False),    
    ([1,2,3], 'ab', 'ab1', True),
    ([1,3,5], 'ab', 'ab', False),        
    ([3,4,5], 'ab1', 'ab1',False),
    ([3,3,3], 'ab2', 'ab3',False),
    ([1,3,5,7], 'ab1', 'ab1', True)    
]


# run all of the NIM tests
for heaps, player1, player2, h in tests:
    play_nim(heaps, player1, player2, h)
    print("\n")

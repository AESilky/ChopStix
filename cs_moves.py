"""
Copyright (c) 2025 AESilky
SPDX-License-Identifier: MIT License
"""

"""
cs_moves.py

This file contains the data for the moves used by the app.

The data is in a tuple of two tuples:
    t1: To hands fingers
    t2: From L and R hands and the move

If a move isn't found for the criteria a random move should be selected.
"""

# Only store the finger combinations once. Leave it up to the algorithm to
# switch the hands and the move if needed.
#
# Don't bother putting in combinations where their isn't a choice or
# difference, the random selection algorithm will handle those.
#
MOVES = ( 
    (
        (1,0),(
            ((4,0),"LL"), # For the win
            ((3,0),"LL"),
            ((2,0),"LR"), # Don't give them 3
            ((1,0),"LL"),
            ((4,1),"LL"), # Win
            ((3,1),"LR"), # Don't give them 2 or 4
            ((2,1),"RL"), # Don't give them 3
            ((1,1),"LL")  # Have them think about splitting
        )
    ),
    (
        (2,0),(
            ((4,0),"LR"), # Don't give them 1
            ((3,0),"LL"), # Win
            ((2,0),"LL"),
            ((1,0),"LL"),
            ((4,1),"RL"), # Don't give them 1
            ((3,1),"LL"), # Win
            ((2,1),"RR"),
            ((1,1),"LL")
        )
    ),
    (
        (1,1),(  # TODO: These were put in for testing. They might need improving.
            ((4,3),"LL"),
            ((4,2),"LL"),
            ((4,1),"LR"),
            ((3,2),"RR"),
            ((3,1),"LL"),
            ((2,1),"LR")
        )
    )
    # TODO: Fill in move moves
)

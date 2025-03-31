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
MOVES:tuple[tuple[tuple[int,int],tuple[tuple[tuple[int,int],str],...]],...] = (  # Tricky/complex annotation.
    (
        (1,0),(
            ((4,0),"LL"), # For the win
            ((3,0),"LL"),
            ((2,0),"LR"), # Don't give them 3
            ((1,0),"LL"),
            ((4,1),"LL"), # Win
            ((3,1),"LR"), # Don't give them 2 or 4
            ((2,1),"RL"), # Don't give them 3
            ((1,1),"LL"), # Have them think about splitting
            ((4,2),"LL"), # Win
            ((3,2),"LR"), # Don't give them 2 or 4
            ((2,2),"RL"), # Don't give them 3
            ((1,2),"LL"), # Have them think about splitting
            ((4,3),"LL"), # Win
            ((3,3),"LR"),
            ((2,3),"RL"), # Don't give them 3
            ((1,3),"LL"), # Don't give them 4. Have them think about splitting
            ((4,4),"LR")  # Win
        )
    ),
    (
        (2,0),(  # TODO: These were put in for testing. They might need improving.
            ((4,0),"LR"),
            ((3,0),"LL"), # Win
            ((2,0),"LL"),
            ((1,0),"LL"),
            ((4,1),"RL"),
            ((3,1),"LL"), # Win
            ((2,1),"RR"),
            ((1,1),"LL"),
            ((4,2),"LL"),
            ((3,2),"LL"), # Win
            ((2,2),"RL"),
            ((1,2),"LL"),
            ((4,3),"RL"), # Win
            ((3,3),"RL"), # Win
            ((2,3),"RL"), # Win
            ((1,3),"RL"), # Win
            ((4,4),"LL")
        )
    ),
    (
        (3,0),(  # TODO: These were put in for testing. They might need improving.
            ((4,0),"LL"),
            ((3,0),"LL"),
            ((2,0),"LL"),
            ((1,0),"LR"),
            ((4,1),"LL"),
            ((3,1),"LL"),
            ((2,1),"LL"),
            ((1,1),"LL"),
            ((4,2),"LL"),
            ((3,2),"LR"),
            ((2,2),"RL"),
            ((1,2),"RL"),
            ((4,3),"LL"),
            ((3,3),"LL"),
            ((2,3),"LL"),
            ((1,3),"RL"),
            ((4,4),"LL")
        )
    ),
    (
        (4,0),(  # TODO: These were put in for testing. They might need improving.
            ((4,0),"LL"),
            ((3,0),"LL"),
            ((2,0),"LL"),
            ((1,0),"LL"),
            ((4,1),"RL"),
            ((3,1),"RL"),
            ((2,1),"RL"),
            ((1,1),"LL"),
            ((4,2),"LL"),
            ((3,2),"RL"),
            ((2,2),"RL"),
            ((1,2),"LL"),
            ((4,3),"LL"),
            ((3,3),"LL"),
            ((2,3),"LL"),
            ((1,3),"LL"),
            ((4,4),"LL")
        )
    ),
    (
        (1,1),(  # TODO: These were put in for testing. They might need improving.
            ((4,0),"LL"),
            ((3,0),"LL"),
            ((2,0),"LL"),
            ((1,0),"LL"),
            ((4,1),"RL"),
            ((3,1),"RL"),
            ((2,1),"RL"),
            ((1,1),"RL"),
            ((4,2),"RR"),
            ((3,2),"LL"),
            ((2,2),"RL"),
            ((1,2),"LL"),
            ((4,3),"LL"),
            ((3,3),"RL"),
            ((2,3),"RR"),
            ((1,3),"LL"),
            ((4,4),"LL")
        )
    ),
    (
        (2,1),(  # TODO: These were put in for testing. They might need improving.
            ((4,0),"LL"),
            ((3,0),"LL"),
            ((2,0),"LL"),
            ((1,0),"LL"),
            ((4,1),"RL"),
            ((3,1),"RL"),
            ((2,1),"RL"),
            ((1,1),"RL"),
            ((4,2),"RR"),
            ((3,2),"LL"),
            ((2,2),"RL"),
            ((1,2),"LL"),
            ((4,3),"LL"),
            ((3,3),"RL"),
            ((2,3),"RR"),
            ((1,3),"LL"),
            ((4,4),"LL")
        )
    ),
    (
        (3,1),(  # TODO: These were put in for testing. They might need improving.
            ((4,0),"LL"),
            ((3,0),"LL"),
            ((2,0),"LL"),
            ((1,0),"LL"),
            ((4,1),"RL"),
            ((3,1),"RL"),
            ((2,1),"RL"),
            ((1,1),"RL"),
            ((4,2),"RR"),
            ((3,2),"LL"),
            ((2,2),"RL"),
            ((1,2),"LL"),
            ((4,3),"LL"),
            ((3,3),"RL"),
            ((2,3),"RR"),
            ((1,3),"LL"),
            ((4,4),"LL")
        )
    ),
    (
        (4,1),(  # TODO: These were put in for testing. They might need improving.
            ((4,0),"LL"),
            ((3,0),"LL"),
            ((2,0),"LL"),
            ((1,0),"LL"),
            ((4,1),"RL"),
            ((3,1),"RL"),
            ((2,1),"RL"),
            ((1,1),"RL"),
            ((4,2),"RR"),
            ((3,2),"RR"),
            ((2,2),"RL"),
            ((1,2),"LL"),
            ((4,3),"LL"),
            ((3,3),"RL"),
            ((2,3),"RR"),
            ((1,3),"LL"),
            ((4,4),"LL")
        )
    ),
    (
        (1,2),(  # TODO: These were put in for testing. They might need improving.
            ((4,0),"LL"),
            ((3,0),"LR"),
            ((2,0),"LL"),
            ((1,0),"LL"),
            ((4,1),"RL"),
            ((3,1),"LR"),
            ((2,1),"RL"),
            ((1,1),"RL"),
            ((4,2),"RR"),
            ((3,2),"LR"),
            ((2,2),"RL"),
            ((1,2),"LL"),
            ((4,3),"LL"),
            ((3,3),"RR"),
            ((2,3),"RR"),
            ((1,3),"RR"),
            ((4,4),"LL")
        )
    ),
    (
        (2,2),(  # TODO: These were put in for testing. They might need improving.
            ((4,0),"LL"),
            ((3,0),"LL"),
            ((2,0),"LL"),
            ((1,0),"LL"),
            ((4,1),"RL"),
            ((3,1),"RL"),
            ((2,1),"RL"),
            ((1,1),"RL"),
            ((4,2),"RR"),
            ((3,2),"LL"),
            ((2,2),"RL"),
            ((1,2),"LL"),
            ((4,3),"LL"),
            ((3,3),"RL"),
            ((2,3),"RR"),
            ((1,3),"LL"),
            ((4,4),"LL")
        )
    ),
    (
        (3,2),(  # TODO: These were put in for testing. They might need improving.
            ((4,0),"LL"),
            ((3,0),"LL"),
            ((2,0),"LL"),
            ((1,0),"LL"),
            ((4,1),"RL"),
            ((3,1),"RL"),
            ((2,1),"RL"),
            ((1,1),"RL"),
            ((4,2),"RR"),
            ((3,2),"LL"),
            ((2,2),"RL"),
            ((1,2),"LL"),
            ((4,3),"LL"),
            ((3,3),"RL"),
            ((2,3),"RR"),
            ((1,3),"LL"),
            ((4,4),"LL")
        )
    ),
    (
        (4,2),(  # TODO: These were put in for testing. They might need improving.
            ((4,0),"LL"),
            ((3,0),"LL"),
            ((2,0),"LL"),
            ((1,0),"LL"),
            ((4,1),"RL"),
            ((3,1),"RL"),
            ((2,1),"RL"),
            ((1,1),"RL"),
            ((4,2),"RR"),
            ((3,2),"LL"),
            ((2,2),"RL"),
            ((1,2),"LL"),
            ((4,3),"LL"),
            ((3,3),"RL"),
            ((2,3),"RR"),
            ((1,3),"LL"),
            ((4,4),"LL")
        )
    ),
    (
        (1,3),(  # TODO: These were put in for testing. They might need improving.
            ((4,0),"LL"),
            ((3,0),"LL"),
            ((2,0),"LL"),
            ((1,0),"LL"),
            ((4,1),"RL"),
            ((3,1),"RL"),
            ((2,1),"RL"),
            ((1,1),"RL"),
            ((4,2),"RR"),
            ((3,2),"LL"),
            ((2,2),"RL"),
            ((1,2),"LL"),
            ((4,3),"LL"),
            ((3,3),"RL"),
            ((2,3),"RR"),
            ((1,3),"LL"),
            ((4,4),"LL")
        )
    ),
    (
        (2,3),(  # TODO: These were put in for testing. They might need improving.
            ((4,0),"LL"),
            ((3,0),"LL"),
            ((2,0),"LL"),
            ((1,0),"LL"),
            ((4,1),"RL"),
            ((3,1),"RL"),
            ((2,1),"RL"),
            ((1,1),"RL"),
            ((4,2),"RR"),
            ((3,2),"LL"),
            ((2,2),"RL"),
            ((1,2),"LL"),
            ((4,3),"LL"),
            ((3,3),"RL"),
            ((2,3),"RR"),
            ((1,3),"LL"),
            ((4,4),"LL")
        )
    ),
    (
        (3,3),(  # TODO: These were put in for testing. They might need improving.
            ((4,0),"LL"),
            ((3,0),"LL"),
            ((2,0),"LL"),
            ((1,0),"LL"),
            ((4,1),"RL"),
            ((3,1),"RL"),
            ((2,1),"RL"),
            ((1,1),"RL"),
            ((4,2),"RR"),
            ((3,2),"LL"),
            ((2,2),"RL"),
            ((1,2),"LL"),
            ((4,3),"LL"),
            ((3,3),"RL"),
            ((2,3),"RR"),
            ((1,3),"LL"),
            ((4,4),"LL")
        )
    ),
    (
        (4,3),(  # TODO: These were put in for testing. They might need improving.
            ((4,0),"LL"),
            ((3,0),"LR"),
            ((2,0),"LL"),
            ((1,0),"LL"),
            ((4,1),"RL"),
            ((3,1),"RL"),
            ((2,1),"RL"),
            ((1,1),"RL"),
            ((4,2),"RR"),
            ((3,2),"RL"),
            ((2,2),"RL"),
            ((1,2),"LL"),
            ((4,3),"LL"),
            ((3,3),"RL"),
            ((2,3),"RR"),
            ((1,3),"LL"),
            ((4,4),"LL")
        )
    ),
    (
        (4,4),(  # TODO: These were put in for testing. They might need improving.
            ((4,0),"LL"),
            ((3,0),"LL"),
            ((2,0),"LL"),
            ((1,0),"LL"),
            ((4,1),"RL"),
            ((3,1),"RL"),
            ((2,1),"RL"),
            ((1,1),"RL"),
            ((4,2),"RR"),
            ((3,2),"LL"),
            ((2,2),"RL"),
            ((1,2),"LL"),
            ((4,3),"LL"),
            ((3,3),"RL"),
            ((2,3),"RR"),
            ((1,3),"LL"),
            ((4,4),"LL")
        )
    )
)

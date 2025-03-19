"""
Copyright (c) 2025 AESilky
SPDX-License-Identifier: MIT License
"""

"""
cs_move_gen.py

This file contains the move generation logic to play, and hopefully win,
the game of ChopStix.

It contains some parameters that allow it to be better or randomly average.
"""
from cs_hands import Hands, Hand
from cs_moves import MOVES  # The best moves to make

from enum import IntEnum, unique
import random  # For our randomness in picking moves

@unique
class YesNoMaybe(IntEnum):
    NO       = 0
    YES      = 1
    MAYBE    = -1

class MoveMaster:
    """
    Contains the parameters that control how aggressively the moves generated
    try to win.
    """

    def __init__(self, favor_split_pcnt=20, favor_random_pcnt=5):  # type: (int,int) -> None
        """
        Create an instance of the game playing move strategy.

        Parameters:
            favor_split_pcnt: int percentage that we should randomly use Split (when we have a choice)
            favor_random_pcnt: int percentage that we choose a random move (when we have a non-split situation)
        """
        # TODO: Add limit checks and raise exception if out of bounds
        self._favor_split = 100 - favor_split_pcnt     # type: int
        self._favor_random = 100 - favor_random_pcnt   # type: int
        # Keep some stats
        self._moves = 0         # type: int
        self._rndmoves = 0      # type: int
        self._rndsplits = 0     # type: int

        return

    @property
    def moves(self):  # type: (None) -> int
        """
        The total number of moves.
        """
        return self._moves

    @property
    def random_moves(self):  # type: (None) -> int
        """
        The number of random moves used.
        """
        return self._rndmoves

    @property
    def random_splits(self):  # type: (None) -> int
        """
        The number of random splits used.
        """
        return self._rndsplits

    #
    # I use a leading underscore on methods that are intended to only be used internally.
    #

    def _pick_move(self, from_hands, to_hands):  # type: (Hands,Hands) -> str
        """
        Pick a non-split move based on the strategy and the value of favoring a random move.

        Parameters:
            from_hands: The hands doing the tapping.
            to_hands: The hands being tapped.

        Return:
            Move string "LL", "LR", "RL" or "RR"
        """
        # Should we select a move or do a random move?
        rnd_int = random.randint(1, 100)
        if self._favor_random <= rnd_int:
            return self._random_move(from_hands, to_hands)
        #
        # Use the MOVES data to select a move...
        #  Note that the MOVES data only contains a single representation of a given
        #   pair of hands fingers - in other words, it doesn't contain both L=1,R-0 and
        #   L=0,R=1. Therefore, it is up to us to switch the hands an check again if a
        #   move isn't found, and to switch the move (from and/or to) if we switched
        #   the hands.
        #
        switch_from = False     # Keep track if we switched the 'from' hands
        from_fingers = (from_hands.left.fingers, from_hands.right.fingers)
        #
        switch_to = False       # Keep track if we switched the 'to' hands
        to_fingers = (to_hands.left.fingers, to_hands.right.fingers)
        move = None             # Move will be set if we find a move
        found_to = False
        found_from = False
        for move_data in MOVES:
            to_has_fingers = move_data[0]  # Get the finger data to check against
            if to_fingers[0] == to_has_fingers[0] and to_fingers[1] == to_has_fingers[1]:
                found_to = True
            elif to_fingers[1] == to_has_fingers[0] and to_fingers[0] == to_has_fingers[1]:  # Check reversed fingers
                found_to = True
                switch_to = True
            if found_to:
                for from_player_move in move_data[1]:
                    from_has_fingers = from_player_move[0]
                    if from_fingers[0] == from_has_fingers[0] and from_fingers[1] == from_has_fingers[1]:
                        found_from = True
                    elif from_fingers[1] == from_has_fingers[0] and from_fingers[0] == from_has_fingers[1]:
                        found_from = True
                        switch_from = True
                    if found_from:
                        # We found a match
                        raw_move = from_player_move[1]
                        if not switch_from:
                            move = raw_move[0]
                        else:
                            move = "R" if raw_move[0] == "L" else "L"
                        if not switch_to:
                            move += raw_move[1]
                        else:
                            move += "R" if raw_move[1] == "L" else "R"
                        break
                break
            if found_to and found_from:
                break
        if move is None:
            move = self._random_move(from_hands, to_hands)
        return move

    def _random_move(self, from_hands, to_hands, split_allowed=False):  # type: (Hands,Hands,bool) -> str
        """
        Generate a random move. Optionally, include split.

        Parameters:
            from_hands: The hands the fingers are coming from.
            to_hands: The hands being tapped.
            split_allowed: Flag indicating if a split move is allowed.

        Return: String of "LL", "LR", "RL", or "RR", or "S" if split is allowed
        """
        move = None
        self._rndmoves += 1
        # If split is allowed, use our 'favor_split' to pick a split or not
        if split_allowed and self._random_split():
            if self._random_split():
                move = "S"
                self._rndsplits += 1
        else:
            # Generate a random, non-split, move
            ## Randomly check the from left or right hand first
            if random.randint(1,2) == 1:
                # See if we can use the left hand
                move = "L" if not from_hands.left.is_fist() else "R"
            else:
                move = "R" if not from_hands.right.is_fist() else "L"
            ## Randomly check the to left or right hand first
            if random.randint(1,2) == 1:
                # See if the left hand has fingers
                move += "L" if not to_hands.left.is_fist() else "R"
            else:
                move += "R" if not to_hands.right.is_fist() else "L"
        return move

    def _random_split(self):  # type: (None) -> bool
        """
        Randomly pick split or not based on our 'favor_split' value.

        Note: Calling code is responsible for knowing is a split is allowed or not.

        Return:
            True: Split
            False: Don't split
        """
        rnd_int = random.randint(1, 100)
        if self._favor_split <= rnd_int:
            return True
        return False

    def _should_split(self, from_hands, to_hands):  # type: (Hands, Hands) -> YesNoMaybe
        if from_hands.can_split():
            # Well, we can split... should we?
            # See if they can win if we don't split
            from_fingers = from_hands.left.fingers + from_hands.right.fingers  # One is 0, so this gives us the hand with fingers
            if from_fingers + to_hands.left.fingers == 5 or from_fingers + to_hands.right.fingers == 5:
                # If we don't split they can win on their next move!
                return YesNoMaybe.YES
            else:
                # See if we can win now if we don't split
                if to_hands.left.is_fist() or to_hands.right.is_fist():
                    if from_fingers + to_hands.left.fingers + to_hands.right.fingers == 5:
                        # We can win. Our 'get_move' logic will figure out how.
                        return YesNoMaybe.NO
                # We can split, but we won't lose if we don't and we won't can't win if we don't
                return YesNoMaybe.MAYBE  # Let the 'move' logic figure out what to do
        return YesNoMaybe.NO  # We can't split

    #
    # Following are the methods intended to be called from outside of the class (no leading underscore)
    #

    def get_move(self, from_hands, to_hands):  # type: (Hands, Hands) -> str
        move = None
        self._moves += 1
        # First, see if we can/should split...
        split = self._should_split(from_hands, to_hands)
        if split == YesNoMaybe.YES:
            move = "S"
        elif split == YesNoMaybe.MAYBE:
            # This indicates that we can split if we want to, but we don't have
            # to, and there isn't a way for us to win in this move.
            #
            # Select split or move based on our favor split parameter
            if self._random_split():
                move = "S"
            else:
                move = self._pick_move(from_hands, to_hands)
        if split == YesNoMaybe.NO:
            # This indicates that we might be able to win. See if we can
            if to_hands.left.is_fist() or to_hands.right.is_fist():
                to_fingers = to_hands.left.fingers + to_hands.right.fingers
                if from_hands.left.fingers + to_fingers == 5:
                    move = "L"  # We will move from the left. Figure out 'to'
                    move += "L" if to_hands.right.is_fist() else "R"
                    return move
                elif from_hands.right.fingers + to_fingers == 5:
                    move = "R"  # We will move from the right. Figure out 'to'
                    move += "L" if to_hands.right.is_fist() else "R"
            if move is None:
                # We can't win, so pick our best move.
                move = self._pick_move(from_hands, to_hands)
        return move


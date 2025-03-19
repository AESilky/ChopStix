"""
Copyright (c) 2025 AESilky
SPDX-License-Identifier: MIT License
"""

"""
cs_hands.py

This file contains the classes to track a Hand and a pair of Hands.
"""
import cs_exceptions as cse

class Hand:
    """
    Models a hand.
    (Note that it isn't based on anything - it is a 'base class')
    """

    # '__init__' (notice that is has two leading and two trailing underscores)
    # is a special method for classes (there are a few). It is called automatically
    # when an instance of the class is created.
    def __init__(self):  # type: (int) -> None
        self._fingers = 1   # I use a leading underscore for class variables to indicate
                            # they shouldn't be changed outside of the class.
        return

    @property
    def fingers(self):  # type: (None) -> int
        """
        The number of fingers out
        """
        return self._fingers

    def add_hand(self, other):  # type: (Hand) -> int
        """
        Adds the fingers of the passed in hand to this hand.
        """
        self._fingers = (self.fingers + other.fingers) % 5
        return self.fingers

    def is_fist(self):  # type: (None) -> bool
        """
        Return True if no fingers are out.
        """
        return (self._fingers == 0)

    def split_to_other_hand(self, other_hand):  # type: (Hand) -> None
        """
        Splits the fingers of this hand to the other.

        Raises a SplitError if this hand doesn't have 2 or 4 fingers
        or the other hand isn't empty.
        """
        if not (self.fingers == 2 or self.fingers == 4):
            # below, I split a source line up using a trailing backslash
            errmsg = "no fingers" if self.fingers == 0 \
                else "1 finger" if self.fingers == 1 \
                else "{} fingers".format(self.fingers)
            raise cse.SplitNotEvenError("From hand has {}.".format(errmsg))
        if not other_hand.fingers == 0:
            raise cse.SplitNotEmptyError("Hand isn't empty.")
        self._fingers = self.fingers // 2  # We use 'integer' divide. To assign, use '_fingers'.
        other_hand._fingers = self.fingers
        return

class Hands:
    """
    Holds two hands, left and right. Provides some operations on the pair.
    """

    def __init__(self):  # type: (None) -> None
        self._left = Hand()     # type: Hand
        self._right = Hand()    # type: Hand
        return

    @property
    def left(self):  # type: (None) -> Hand
        return self._left

    @property
    def right(self):  # type: (None) -> Hand
        return self._right

    def can_split(self):  # type: (None) -> bool
        """
        Check if the hands can be split.
        True: They can
        False: They cannot
        """
        can = False  # Assume we can't split
        if self._left.is_fist() or self._right.is_fist():
            # First criteria met, check that the other hand has an even number of fingers.
            if (not self._left.is_fist() and self._left.fingers % 2 == 0) \
                or (not self._right.is_fist() and self._right.fingers % 2 == 0):
                # I use 'ZZZ' to mark things that really MUST BE DONE for the app to work. These block a release.
                # I use 'zzz' to mark things that SHOULD be done for it to work well. These could block a release.
                # I use 'TODO:' to mark things that would improve it or be nice to have. These don't affect a release.
                # That way, a global search can be used and things can be addressed as needed.
                can = True
        return can

    def split(self):  # type: (None) -> None
        if self._left.fingers == 0:
            self._right.split_to_other_hand(self._left)
        else:
            self._left.split_to_other_hand(self._right)
        return

"""
Copyright (c) 2025 AESilky
SPDX-License-Identifier: MIT License
"""

"""
cs_game.py

This file contains the classes that implement the logic of the game, as
well as the high-level start/play/finish flow.
"""
import cs_exceptions as cse  # This imports everything with an alias of 'cse'
from cs_hands import Hand, Hands  # This specifically imports classes that we will use
from cs_score import Score  # Specific class
from cs_move_gen import MoveMaster  # The game play strategy

import math  # Used for calculating the number of digits that will be displayed for stats
import time  # Used for sleeping. No alias is specified, so use will be 'time.xxx'

__version__ = '1.0.1'  # Version information for this module (this is a 'special' value in Python)

# Values that are intended to be constants use all caps (by convention)
#
SHORT_PAUSE = 0.8   # Number of seconds to pause for a short break.
LONG_PAUSE = 1.3    # Number of seconds to pause for a long break.

# You will see that I use 'CamelCase' for my class names. Just a convention
# that I follow (and many others do too).


def display_hands(us, them):  # type: (Hands, Hands) -> None
    """
    Displays a representation of four hands, two from each player.

    Parameters:
        us: Our hands
        them: Their hands

    Note: Notice that this is a 'module method', as it isn't part of a class.
    """
    our_left_fingers = (' ' * (4 - us.left.fingers)) + ('I' * us.left.fingers)
    our_right_fingers = 'I' * us.right.fingers
    their_left_fingers = (' ' * (4 - them.left.fingers)) + ('I' * them.left.fingers)
    their_right_fingers = 'I' * them.right.fingers
    print("  |  |>    <|  |  [My Hands]")
    print("  wwww      wwww")
    print("  {}      {}".format(our_left_fingers, our_right_fingers))
    print("")
    print("  {}      {}".format(their_left_fingers, their_right_fingers))
    print("  mmmm      mmmm")
    print("  |  |>    <|  |  [Your Hands]")
    return

def display_stats(moves, rnd_moves, rnd_splits):  # type: (int,int,int) -> None
    """
    Display (print) statistics about the gaem.

    Parameters:
        moves: The number of moves (total)
        rnd_moves: The number of times the move was random
        rnd_splits: The number of times using split was random
    """
    width = int(math.log10(moves)) + 1  # The number of digits in the moves value
    print("        My Moves: {1:>{0}d}".format(width, moves))
    print(" My Random Moves: {1:>{0}d}".format(width, rnd_moves))
    print("My Random Splits: {1:>{0}d}".format(width, rnd_splits))
    return

class Game:
    """
    Implements the start/play/finish flow.
    """

    def __init__(self):  # type: (None) -> None
        self._us = Hands()          # type: Hands  # Create an instance of a hands for us
        self._them = Hands()        # type: Hands  # and them
        self._score = Score()       # type: Score
        self._moves_this_game = 0   # type: int
        return

    def move(self, from_hands, to_hands, move_cmd):  # type: (Hands, Hands, str) -> None
        """
        Process the move command and move from the 'from hands' to the 'to hands'.

        move_cmd: Expected to be uppercase.

        Raises:
            InvalidMoveCmd error if the command isn't valid (not an S or a
            combination of 'L' and 'R').

            MoveNotAllowed error if the move specified isn't appropriate for
            the hands.
        """
        if move_cmd == 'S':
            # See if a split is valid (only uses the 'from_hands')
            if from_hands.can_split():
                from_hands.split()
            else:
                raise cse.MoveNotAllowed("The fingers, [{},{}] don't allow for a split.".format(from_hands.left.fingers, from_hands.right.fingers))
        elif move_cmd == "LL" or move_cmd == "LR":
            if not from_hands.left.fingers == 0:
                if move_cmd == "LL":
                    to_hands.left.add_hand(from_hands.left)
                else:
                    to_hands.right.add_hand(from_hands.left)
            else:
                raise cse.MoveNotAllowed("There are no fingers on the left hand.")
        elif move_cmd == "RL" or move_cmd == "RR":
            if not from_hands.right.fingers == 0:
                if move_cmd == "RL":
                    to_hands.left.add_hand(from_hands.right)
                else:
                    to_hands.right.add_hand(from_hands.right)
            else:
                raise cse.MoveNotAllowed("There are no fingers on the right hand.")
        else:
            raise cse.InvalidMoveCmd(move_cmd)
        return

    def play(self):  # type: (None) -> None
        """
        Play the game.
        """
        game_strategy = MoveMaster()
        playing = True
        self._score.start_game()
        self._moves_this_game = 0
        # TODO: Add option to let them go first or have us go first.
        their_move = True
        while playing:
            print("")
            display_hands(self._us, self._them)
            self._moves_this_game += 1
            if their_move:
                while their_move:
                    # Their turn...
                    s = input("\nYour move: ")  # TODO: Include in the prompt the moves that are valid.
                    su = s.replace(" ", "").upper()  # Remove spaces and make it uppercase so it is more regular to work with
                    if su == 'Q':
                        their_move = False
                        playing = False
                        continue  # This causes the loop to start again.
                    # TODO: Implement 'new game'
                    # zzz: Implement giving them 'help'
                    # TODO: Implement a way for them to ask for a suggestion.
                    # TODO: Implement a way to ask how the computer's move was determined (S,Table,Random)
                    else:  # Treat it as a move
                        try:
                            self.move(self._them, self._us, su)
                            their_move = False
                            if self.they_won_check():
                                time.sleep(LONG_PAUSE)
                                playing = False
                                # TODO: Implement an option to play another game
                        except cse.InvalidMoveCmd as ex1:
                            print("The move you entered, '{}' is not valid.".format(s))
                            print("Only use the letters 'S' or 'L' and 'R' to specify your move. Enter '?' for help.")
                            time.sleep(0.8)
                        except cse.MoveNotAllowed as ex2:
                            print("That move isn't allowed. {}".format(ex2.reason))
                            time.sleep(0.8)
            else:
                # Our turn...
                move = game_strategy.get_move(self._us, self._them)
                time.sleep(LONG_PAUSE)
                print("\n\n>>> My move is: {}".format(move))
                self.move(self._us, self._them, move)
                their_move = True
                if self.we_won_check():
                    time.sleep(LONG_PAUSE)
                    playing = False
                    # TODO: Implement an option to play another game
        print("")
        display_stats(game_strategy.moves, game_strategy.random_moves, game_strategy.random_splits)
        return

    def they_won_check(self):  # type: (None) -> bool
        """
        Check to see if they won.

        If they did, update the score and congratulate them.

        Returns:
            True if they won.
            False if they didn't
        """
        if self._us.left.is_fist() and self._us.right.is_fist():
            self._score.team_b_won()
            # TODO: Pick from a variety of messages to say they win.
            print("Congratulations, you won! It took {} moves".format(self._moves_this_game))
            return True  # I like to only have a single return point (at the end)
                            # but some programmers use multiple - like this.
        return False

    def we_won_check(self):  # type: (None) -> bool
        """
        Check to see if we won.

        If we did, update the score and console them.

        Return: True if we won. False if we didn't
        """
        rv = False  # This will be the return value (for a single return statement)
        if self._them.left.is_fist() and self._them.right.is_fist():
            self._score.team_a_won()
            # TODO: Pick from a variety of messages to say we win.
            print("I win, I win!!! Oh, sorry that you lost. It took {} moves".format(self._moves_this_game))
            rv = True
        return rv

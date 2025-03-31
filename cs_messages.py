"""
Copyright (c) 2025 AESilky
SPDX-License-Identifier: MIT License
"""

"""
cs_messages.py

This file contains the (static) main text for the app.
"""

# In classes I (try to) keep my methods in alphabetical order, but in non-class Python
# code, they need to be defined before they are used, so that dictates the order to
# some extent.

def help() -> None:  # The `-> None` is a 'type annotation' it lets the IDE know what the method takes and what it returns. Not required, but helpful.
    """
    Prints a description of the game.
    """
    # Here we will print multiple lines with a single print statement
    print("We each start with one finger out on each hand. We take turns tapping\n"
        + "one of our hands on one of the other player's hands. The number of fingers\n"
        + "on our hand are added to the number of fingers on the other player's hand,\n"
        + "and the result (modulo 5) is then on the other player's hand. For example,\n"
        + "if a hand with two fingers out is 'tapped' on a hand with four fingers out,\n"
        + "the result is the 'tapped' hand has one finger out. (2 + 4 = 6. 6 modulo 5 = 1)\n"
        + "\n"
        + "In addition to tapping the other player's hand, an alternate move called\n"
        + "'split' is possible if the player has one hand with no fingers out and one\n"
        + "hand with either two or four fingers out. The result is to split the number\n"
        + "of fingers between the two hands. After a split, it becomes the other player's\n"
        + "turn (to tap or split).\n")
    return  # Technically, not needed. But I like to include it to make the end clear.

def options(show_split:bool=False, show_new:bool=False, show_quit:bool=False) -> None:  # `:bool` are also 'type annotations`
    """
    Prints the options available to the user.
    """
    print("At any prompt you can enter a '?' to get help.")
    print("")
    print("To make a move, enter two letters. The first letter is your hand,")
    print("'L'eft or 'R'ight, and the second letter is my hand that you are tapping")
    print("(as you see them - in other words, your left or right).")
    print("")
    if (show_split):
        print("To split, enter 'S'")
        print("")
    # Next, use conditional assignments into variables...
    ntext = "To start a new game, enter 'N'." if show_new else ""
    qtext = "To quit, enter 'Q'." if show_quit else ""
    # Format a string with the two optional texts...
    t = "{} {}".format(ntext, qtext)
    print(t)
    return

def intro() -> None:
    """
    Displays an introduction of the game and how it's played.
    """
    print("The game is played with our two (virtual) hands.")
    help()  # Print the help information
    print("")
    print("The game continues back and forth until one player's tapping results in the")
    print("other player not having any fingers out. In other words...")
    print("The other player is 'tapped out!'")
    print("")
    # Print the options...
    options(True, show_quit=True, show_new=True)  # Pass 'True' (by order) to show 'split' option, the others by name (not in order)
    return


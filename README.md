# The Game of ChopStix

This is the (somewhat) classic game of ChopStix, where two players challenge
their math reasoning skills, to try to tap out their opponent by getting
all of their fingers out of play.

The players start with a single finger out on each hand. The first player
'taps' one of the other player's hands with one of their hands. The number
of fingers on the 'from' hand are added to the 'to' hand. Of course, the
first move will result in two fingers on one of the opponent's hands. It
is then the second player's turn. The addition is done modulo 5, For example,
if 2 fingers are tapped on 4 fingers the result is 1 finger.

The game continues until one of the players is 'tapped out' - in other words,
they don't have any fingers out on either hand.

## Play Against the Computer

This application allows a player to challenge the computer. The application
provides some instructions when it starts, so we won't repeat them here.

The application has a playing strategy and a set of moves that are used
for its play. There are options to factor in some random moves even when
a specific move exists in its move data, as well as random moves for the
cases when the move doesn't exist in the data.

## Running the Application

In a command prompt where Python 3 is available (named 'python3'):
>`python3 ChopStix.py`

On Windows, Python3 might be just 'python'. Test by using the command:
>`python -V`
If this lists a 3.x version, use:
>`python ChopStix.py`

## Learning Python

The goal of this application is to provide a (hopefully) fun way to read
through some Python code to understand how it works. Hopefully, in doing
this some knowledge of Python is picked up.

There is no claim that this is PERFECT Python code, but it is a fully-
featured application and is written with a reasonable amount of error
checking and handling (as opposed to the way many training examples are
written). It is also written in a style that is typical of what you may
encounter with commercial applications.

## Exercises

Beyond generally reviewing the code, there are a number of TODO's scattered
about. Some are to implement missing features, some are suggestions for
additional features, and some would be to add or improve the computer's
play.

## Style

As is typical with applications with some amount of complexity, this
application is split between multiple files. Hopefully the split makes sense
to those perusing the code. The Python file containing the 'main' method
starts with an uppercase letter, while the non-main files are lowercase.

## Code Updates

Since one of the goals is to provide an application that can be used for
learning/training, updates that implement the TODOs will most likely
not be incorporated into the main branch. Different approaches to the
TODOs might be put into easily identified branches.

If there are changes that would make the learning/training aspect better,
they will be considered for inclusion in the main branch.

Please keep this in mind if you submit a PR.

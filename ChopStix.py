#!/usr/bin/env python3
"""
MIT License

Copyright (c) 2025 AESilky

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

"""
ChopStix.py

Classic game of ChopStix played between a user (at the keyboard) and the
computer. The computer will sometimes randomly pick moves to give the user
a fighting chance. The move 'strategy' data is in a separate file to
minimize the chance of modifying the code when the strategy is edited.
"""


import cs_messages as msgs  # Import the messages and use an alias
from cs_game import Game
# I like putting a blank line between my own code's imports and system or 3rd-party imports

import sys
import traceback  # This is kind of advanced - but I'll use it so you see how it can be used.

def main():
    # TODO: Process command-line options to allow setting the randomness of the move generator.
    print("\nWelcome to the game of ChopStix.")  # The '\n' prints a new line
    print("It is an interesting math challenge between you and me.")
    print("")
    msgs.intro()
    game = Game()
    game.play()
    return  # Technically, not needed. But I like to include it to make the end clear.

if __name__ == "__main__":  # This tests to see if we are being called as the 'main' program
    exit_status = 1  # Command-line applications often return non-zero to indicate an error.
    try:
        main()  # If so, execute the 'main' method.
        exit_status = 0  # Returning from main means all is good.
    except KeyboardInterrupt:
        exit_status = 0  # We will also treat Ctrl-C as an acceptable exit.
    except Exception as ex:
        print("\nAn error was encountered: {}\n\n".format(ex))
        print(traceback.format_exc())
    sys.exit(exit_status)


"""
Copyright (c) 2025 AESilky
SPDX-License-Identifier: MIT License
"""

"""
cs_score.py

This file contains a class that implement a fairly simple score keeper.
"""

class Score:
    """
    Keeps score for us and them.
    """

    def __init__(self):  # type: (None) -> None
        self._team_a = 0    # type: int
        self._team_b = 0    # type: int
        self._games = 0     # type: int
        return

    @property
    def team_a(self):  # type: (None) -> int
        return self._team_a

    @property
    def team_b(self):  # type: (None) -> int
        return self._team_b

    @property
    def games(self):  # type: (None) -> int
        return self._games

    def start_game(self):  # type: (None) -> None
        """
        Increment the number of games and clear the scores.
        """
        self._team_a = 0
        self._team_b = 0
        self._games += 1
        return

    def team_a_won(self):  # type: (None) -> None
        """
        Increment Team A's score.
        """
        self._team_a += 1
        return

    def team_b_won(self):  # type: (None) -> None
        """
        Increment Team B's score.
        """
        self._team_b += 1
        return


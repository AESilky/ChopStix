"""
Copyright (c) 2025 AESilky
SPDX-License-Identifier: MIT License
"""

"""
cs_exceptions.py

This file contains the classes that represent the Exceptions/Errors for the app.
"""

# You will see that I use 'CamelCase' for my class names. Just a convention
# that I follow (and many others do too).

class InvalidMoveCmd(ValueError):
    """
    Indicates that the move entered wasn't an 'S' or a combination of 'L' and 'R'.
    """
    pass

class MoveNotAllowed(Exception):
    """
    Indicates that the move isn't possible given the hands.
    """
    def __init__(self, reason):  # type: (str) -> None
        self._reason = reason
        super().__init__(self._reason)
        return

    @property
    def reason(self):  # type: (None) -> str
        """
        The reason the move is not allowed.
        """
        return self._reason

class SplitError(Exception):
    """
    Base error for split problems. It is based on the system's 'Exception' class.
    """
    pass

class SplitNotEvenError(SplitError):
    """
    Split error indicating the source hand didn't have 2 or 4 fingers.
    (it is a type of 'SplitError')
    """
    pass

class SplitNotEmptyError(SplitError):
    """
    Split error indicating the destination hand isn't empty
    (it is a type of 'SplitError')
    """
    pass


"""
Find the total number of patterns of the Android lock screen. The number
of key used has to be at least 4, and max 9.

Example:

use 5 keys:
OAB
OOC
OED

OAB
OCD
OOE

Same thing goes with 4, 6, 7, 8, 9 keys. Count the total possible pattern.
The order of keys used matters.

Rules:

At-least 4 and at-max 9 dots must be connected.
There can be no jumps
Once a dot is crossed, you can jump over it.
"""


class Solution(object):
    def numberOfPattern(self):
        
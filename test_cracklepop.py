"""
Write a program that prints out the numbers 1 to 100 (inclusive).
If the number is divisible by 3, print Crackle instead of the number.
If it's divisible by 5, print Pop. If it's divisible by both 3 and 5,
print CracklePop.
"""

import pytest
from cracklepop import cracklepop_determiner


def test_basics():

    assert cracklepop_determiner(3) == 'Crackle'

    assert cracklepop_determiner(5) == 'Pop'

    assert cracklepop_determiner(3*5) == 'CracklePop'

    assert cracklepop_determiner(1) == '1'

    assert cracklepop_determiner(1) == '1'
"""
Write a program that prints out the numbers 1 to 100 (inclusive).
If the number is divisible by 3, print Crackle instead of the number.
If it's divisible by 5, print Pop. If it's divisible by both 3 and 5,
print CracklePop.
"""

import pytest

def cracklepop_determiner(number):
    print_statement = ''
    if number % 3 == 0: 
        print_statement = 'Crackle'

    if number % 5 == 0:
        print_statement = 'Pop'

    if (number % 3 == 0) and (number % 5 == 0):
        print_statement = 'CracklePop'

    if print_statement == '':
        print_statement = str(number)
    return print_statement

def cracklepop():
    for ii in range(1,101):
        print_statement = cracklepop_determiner(ii)
        print(print_statement)

def test_basics():

    assert cracklepop_determiner(3) == 'Crackle'

    assert cracklepop_determiner(5) == 'Pop'

    assert cracklepop_determiner(3*5) == 'CracklePop'

    assert cracklepop_determiner(1) == '1'

    assert cracklepop_determiner(1) == '1'

def test_multiples():

    for ii in range(1, 101):
        if 



# cracklepop()
# cracklepop_test()
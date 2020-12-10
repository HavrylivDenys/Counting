from typing import Union


def counting_holes(v: Union[str, int]) -> int:
    """ Counting holes functions excepts string or integer value and returns the number of 'holes' in numbers.
    If it is not a string with number or not an integer value function returns string 'Error'
    counting_holes('08824') => 5 
    counting_holes(88) => 4
    counting_holes(99.3) => 'Error'
    counting_holes('abc') => 'Error' """
    return v


print(help(counting_holes))

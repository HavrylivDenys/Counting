from typing import Union, Pattern, Match, Dict
from re import match, compile


def counting_holes(v: Union[str, int]) -> int:
    """ 
    Counting holes functions excepts string or integer value and returns the number of 'holes' in numbers.
    If it is not a string with number or not an integer value function returns string 'Error'
    counting_holes('08824') => 5
    counting_holes(88) => 4
    counting_holes(99.3) => 'Error'
    counting_holes('abc') => 'Error' 
    """

    value: str = str(v)
    is_str_or_int: bool = check(value)

    if is_str_or_int:
        return count(value)
    else:
        return "Error"


def check(v: str) -> bool:
    """ 
    Check function validates the data. It returns True if variable is string with integers or integer.
    It returns False in any other way.
    check('08824') => True
    check('88') => True
    check('99.3') => False
    check('abc') => False 
    """

    pattern: Pattern = compile(r'^\d+$')
    check: Match = match(pattern, v)

    if check:
        return True

    return False


def count(v: str) -> int:
    """ 
    Count function counts the holes in string. It returns the sum of holes in numbers.
    count('08824') => 5
    count('88') => 4
    count('11') => 0
    count('00021') => 0 
    """

    value: str = v.lstrip("0")
    result: int = 0

    numbers: Dict[str, int] = {
        "0": 1,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 1,
        "5": 0,
        "6": 1,
        "7": 0,
        "8": 2,
        "9": 1,
    }

    for ch in value:
        result = result + numbers[ch]

    return result


def test() -> None:
    print(counting_holes("08842"))
    print(counting_holes([]))
    print(counting_holes(88))
    print(counting_holes("00021"))
    print(counting_holes(11))
    print(counting_holes(20.4))


test()

from typing import Union, Pattern, Match, Dict
from re import match, compile


def counting_holes(v: Union[str, int]) -> int:
    """ 
    Counting holes functions excepts string or integer value and returns the number of 'holes' in numbers.

    Parameters
    ----------
    v : str, int
        The string or number for counting
    Returns
    -------
    int
        A number of holes in numbers of string.
    """

    value: str = str(v)
    is_str_or_int: bool = check(value)

    if is_str_or_int:
        return count(value)
    else:
        return "Error"


def check(v: str) -> bool:
    """ 
    Check function validates the data. It returns True if variable is string with integers or when variable is an integer number.

    Parameters
    ----------
    v : str
        The string for check. Validate the condition. Condition -> integer numbers. 
    Returns
    -------
    bool
        True or False
    """

    pattern: Pattern = compile(r'^\d+$')
    check: Match = match(pattern, v)

    if check:
        return True

    return False


def count(v: str) -> int:
    """ 
    Count function counts the holes in string.

    Parameters
    ----------
    v : str
        The string for holes calculation.
    Returns
    -------
    int
        The number of holes
    """

    # Striping leading zeros
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

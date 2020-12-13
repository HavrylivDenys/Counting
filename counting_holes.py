from typing import Union, Pattern, Match, Dict
from re import match, compile


def counting_holes(v: Union[str, int]) -> int:
    """
    Counting holes functions excepts string or integer value
    and returns the number of 'holes' in numbers.

    Parameters
    ----------
    v : str, int
        The string or number for counting
    Returns
    -------
    int
        A number of holes in numbers of string.
    """

    if isinstance(v, (int, str)):
        try:
            value = str(abs(int(v)))
        except ValueError:
            return 'Error'
    else:
        return 'Error'

    return count(value)


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

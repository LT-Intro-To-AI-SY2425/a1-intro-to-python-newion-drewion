"""Assignment 1

Fill in the following function skeletons - descriptions are provided in 
the docstring (the triple quote thing at the top of each function)

Some assert statements have been provided - write more of them to test your code!

The `raise NotImplementedError(...)`s are placeholders to help you not skip implementing
a function. They should be removed and replaced with your solution.

This portion of the assignment will not be graded, but this gives you some problems to 
check, if you do not complete the generative AI portion of the assignment.
"""
import math
from typing import List, TypeVar


def absolute(n: int) -> int:
    """Gives the absolute value of the passed in number. Cannot use the built in
    function `abs`.

    Args:
        n - the number to take the absolute value of

    Returns:
        the absolute value of the passed in number
    """
    n = int(input("number here: "))
    if n>0:
        return n
    else:
        n = n*-1
    return n
    
def factorial(n: int) -> int:
    """Takes a number n, and computes the factorial n! You can assume the passed in
    number will be positive

    Args:
        n - the number to compute factorial of

    Returns:
        factorial of the passed in number
    """

    n = int(input("number here:"))
    n = math.factorial(n)
    return n 

T = TypeVar("T")


def every_other(lst: List[T]) -> List[T]:
    """Takes a list and returns a list of every other element in the list, starting with
    the first.

    Args:
        lst - a list of any (constrained by type T to be the same type as the returned
            list)

    Returns:
        a list of every of other item in the original list starting with the first
    """
    return lst[::2]



def sum_list(lst: List[int]) -> int:
    """Takes a list of numbers, and returns the sum of the numbers in that list. Cannot
    use the built in function `sum`.

    Args:
        lst - a list of numbers

    Returns:
        the sum of the passed in list
    """
    summ = 0
    for i in lst:
        summ += i
    return summ     

def mean(lst: List[int]) -> float:
    """Takes a list of numbers, and returns the mean of the numbers.

    Args:
        lst - a list of numbers

    Returns:
        the mean of the passed in list
    """
    sum2 = 0
    for i in lst:
        sum2 += i
    sum2 = sum2/len(lst)
    return sum2


def median(lst: List[int]) -> float:
    """Takes an ordered list of numbers, and returns the median of the numbers.

    If the list has an even number of values, it computes the mean of the two center
    values.

    Args:
        lst - an ordered list of numbers

    Returns:
        the median of the passed in list
    """
    length = len(lst)

    halfLength = length // 2

    if length % 2 == 1:
        return float(lst[halfLength])
    else:
        return (lst[halfLength - 1] + lst[halfLength]) / 2.0

def duck_duck_goose(lst: List[str]) -> List[str]:
    i = 0  # Start at the beginning of the list

    # Continue until only two names are left
    while len(lst) > 2:
        # Determine the index of the name to be removed
        i = (i + 2) % len(lst)  # Move 2 steps forward (since the count starts at 1)
        lst.pop(i)  # Remove the name at the current index

    return lst

    



# this line causes the nested code to be skipped if the file is imported instead of run
if __name__ == "__main__":
    assert absolute(-1) == 1, "absolute of -1 failed"
    assert factorial(4) == 24, "factorial of 4 failed"
    assert every_other([1, 2, 3, 4, 5]) == [
        1,
        3,
        5,
    ], "every_other of [1,2,3,4,5] failed"
    assert sum_list([1, 2, 3]) == 6, "sum_list of [1,2,3] failed"
    assert mean([1, 2, 3, 4, 5]) == 3, "mean of [1,2,3,4,5] failed"
    assert median([1, 2, 3, 4, 5]) == 3, "median of [1,2,3,4,5] failed"

    names = ["roscoe", "kim", "woz", "solin", "law", "remess"]
    assert duck_duck_goose(names) == ["roscoe", "law"]

    print("All tests passed!")
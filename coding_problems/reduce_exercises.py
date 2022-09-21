"""
List of exercises on reduce() function.

Python’s reduce() is a built-in function that performs computation on all the elements
in an iterable (such as array, list, etc.) and returns a single computed value.

Syntax:
reduce(function, iterable, [initializer])

Parameters:
    function: Required. The function to execute for each item. Function must have one parameter.
    iterable: Required. An object that represents a series, collection, or iterator. Accepts many iterables.
    initializer: Optional. It's placed before the items of the iterable, and serves as a default
                 when the iterable is empty.
"""

from functools import reduce

class ReduceExercises(object):
    def __int__(self):
        """Constructor."""
        pass

    @staticmethod
    def sum_elements(nums):
        """Returns the total sum of all the elements from an iterable."""
        return reduce(lambda a, b: a + b, nums)


if __name__ == "__main__":
    pass

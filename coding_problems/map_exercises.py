"""
List of exercises on map() function.

Python’s map() is a built-in function that allows us to process and transform all the elements
in an iterable (such as array, list, etc.) without requiring an explicit for loop.

Syntax:
map(function, iterable, ...)

Parameters:
    function: Required. The function to execute for each item. Function must have one parameter.
    iterable: Required. An object that represents a series, collection, or iterator. Accepts many iterables.

Note: map() function returns an "iterable" map object, but it does not print. Therefore, we have
to wrap the map() result in list() for printing like this: list(map()).
"""


class MapExercises(object):
    def __init__(self):
        """Constructor."""
        pass

    @staticmethod
    def find_element_length(str):
        """Returns the length of each element in an iterator."""
        return list(map(lambda e: len(e), str))

    @staticmethod
    def double_numbers(nums):
        """Doubled the elements in an array."""
        return list(map(lambda e: e * 2, nums))


if __name__ == "__main__":
    fruits = ["apple", "orange", "banana", "pineapple"]
    nums = [3, 4, 8, 9, 12, 7]

    print(MapExercises.find_element_length(fruits))
    print(MapExercises.double_numbers(nums))

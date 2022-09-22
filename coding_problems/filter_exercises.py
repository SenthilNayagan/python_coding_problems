"""
List of exercises on filter() function.

Python’s filter() is a built-in function that allows us to process and filter all the elements
in an iterable (such as array, list, etc.) and returns a subset of the elements.

Syntax:
filter(function, iterable, ...)

Parameters:
    function: Required. The function to execute for each item. Function must have one parameter.
    iterable: Required. An object that represents a series, collection, or iterator. Accepts many iterables.

Note: filter() function returns an "iterable" map object, but it does not print. Therefore, we have
to wrap the filter() result in list() for printing like this: list(filter()).
"""


class FilterExercises(object):
    def __init__(self):
        """Constructor."""
        pass

    @staticmethod
    def find_even_numbers(nums):
        """Returns even numbers."""
        return list(filter(lambda e: e%2 == 0, nums))

    @staticmethod
    def extract_vowels(str):
        """Extracts vowels from the string."""
        vowels = "aeiou"
        return list(filter(lambda e: e in vowels, str))


if __name__ == "__main__":
    print(FilterExercises.extract_vowels("pineapple"))
    print(FilterExercises.extract_vowels("banana"))
    print(FilterExercises().extract_vowels("pineapple"))

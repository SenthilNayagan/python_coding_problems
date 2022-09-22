"""
Various numbers related exercises.
"""


from functools import reduce


class NumbersExercises(object):
    def __init__(self):
        """Constructor."""
        pass

    @staticmethod
    def swap_values(x, y):
        x, y = x, y
        y, x = x, y
        return x, y

    @staticmethod
    def flatten_nested_list(nested_nums):
        return [element for sublist in nested_nums for element in sublist]

    @staticmethod
    def find_max(nums) -> int:
        return reduce(lambda x, y: x if x > y else y, nums)


if __name__ == "__main__":
    print(NumbersExercises.swap_values(6, 5))

    nested_list = [[1], [2, 3], [4, 5, 6, 7]]
    print(NumbersExercises.flatten_nested_list(nested_list))

    lst = [2, 3, 5, 6, 100, 23, 21]
    print(NumbersExercises.find_max(lst))

    print(NumbersExercises.find_max([4, 1, 7, 5, 9, 12]))
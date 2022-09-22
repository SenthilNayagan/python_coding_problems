"""
Various numbers related exercises.
"""


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


if __name__ == "__main__":
    print(NumbersExercises.swap_values(6, 5))

    nested_list = [[1], [2, 3], [4, 5, 6, 7]]
    print(NumbersExercises.flatten_nested_list(nested_list))

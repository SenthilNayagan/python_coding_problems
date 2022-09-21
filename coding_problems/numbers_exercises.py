"""
Various numbers related exercises.
"""


class NumbersExercises(object):
    def __int__(self):
        """Constructor."""
        pass

    @staticmethod
    def swap_values(x, y):
        x, y = x, y
        y, x = x, y
        return x, y


if __name__ == "__main__":
    print(NumbersExercises.swap_values(6, 5))

"""
Various string related exercises.
"""


class StringExercises(object):
    def __init__(self):
        """Constructor."""
        pass

    @staticmethod
    def string_multiplication(str, times):
        return str * times

    @staticmethod
    def shif_chars(str, shift_by):
        return list(map(lambda c: chr(ord(c) + shift_by), str))


if __name__ == "__main__":
    print(StringExercises.string_multiplication("Hello ", 5))
    print(StringExercises.shif_chars(['a', 'b', 'c'], 2))

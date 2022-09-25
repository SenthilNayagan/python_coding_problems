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
    def shift_chars(str, shift_by):
        return list(map(lambda c: chr(ord(c) + shift_by), str))

    @staticmethod
    def string_permutation(s, pocket=""):
        """Gets all the permutation of the given string.

        Time complexity:
        Space complexity:
        """
        if len(s) == 0:
            return pocket
        else:
            for i in range(len(s)):
                c = s[i]
                front = s[0:i]
                back = s[i+1:]
                together = front + back
                StringExercises.string_permutation(together, c + pocket)


if __name__ == "__main__":
    print(StringExercises.string_multiplication("Hello ", 5))
    print(StringExercises.shift_chars(['a', 'b', 'c'], 2))

    print(StringExercises.string_permutation("ABCD", ""))

"""
Various numbers related exercises.
"""


from functools import reduce


class NumbersExercises(object):
    def __init__(self):
        """Constructor."""
        pass

    def swap_values(self, x, y):
        x, y = x, y
        y, x = x, y
        return x, y

    def flatten_nested_list(self, nested_nums):
        return [element for sublist in nested_nums for element in sublist]

    def find_max(self, nums) -> int:
        return reduce(lambda x, y: x if x > y else y, nums)

    def add_two_lists(self, l1, l2) -> list:
        """Sum two lists."""
        out = []
        if len(l1) != len(l2):
            if len(l1) > len(l2):
                l2.extend([0] * (len(l1) - len(l2)))
            else:
                l1.extend([0] * (len(l2) - len(l1)))

        reminder = 0
        for i in range(len(l1)):
            total = l1[i] + l2[i] + reminder

            if total > 9:
                once = total - 10
                tens = total // 10
                out.append(once)
                reminder = tens
            else:
                out.append(total)
                reminder = 0
        out[len(l1) - 1] = out[len(l1) - 1] + reminder
        return out

    def reverse_number_bad_smell(self, num):
        """
        Code smell: Doesn't work well for -ve numbers.
        Also, no boundary checks are done.
        """
        reversed_num = 0

        while num != 0:
            digit = num % 10
            reversed_num = reversed_num * 10 + digit
            num //= 10  # Floor division
        return reversed_num

    def reverse_number_optimized(self, num):
        is_negative = False

        if num < 0:
            is_negative = True
            num = -num  # Changing to +ve value and continue below.

        reversed_num = 0

        while num:
            digit = num % 10
            reversed_num = reversed_num * 10 + digit
            num //= 10

        if reversed_num >= 2 ** 31 - 1 or reversed_num <= -2 ** 31:
            return 0

        return -reversed_num if is_negative else reversed_num  # Ensure to prefix -ve sign if the given num is < 0.

    def tuple_update_mutable_elements(self, n: tuple) -> tuple:
        # my_tuple = (4, 2, 3, [6, 5])
        # my_tuple[3][0] = 9    # Output: (4, 2, 3, [9, 5])
        pass

    def move_zeros_towards_end(self, seq):
        """Move all the zeros towards end of the given list.

        Time complexity:
        Space complexity:
        """
        out = list(filter(lambda e: e != 0, seq))
        out.extend([0] * seq.count(0))
        return out


if __name__ == "__main__":
    obj = NumbersExercises()
    print(obj.swap_values(6, 5))

    nested_list = [[1], [2, 3], [4, 5, 6, 7]]
    print(obj.flatten_nested_list(nested_list))

    lst = [2, 3, 5, 6, 100, 23, 21]
    print(obj.find_max(lst))

    print(obj.find_max([4, 1, 7, 5, 9, 12]))

    print(obj.add_two_lists([9,9,9,9,9,9,9], [9,9,9,9]))

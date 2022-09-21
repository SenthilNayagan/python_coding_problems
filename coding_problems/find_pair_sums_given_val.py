"""
Problem: Find pair that sums up to “k”.

Description:
Given an array of integers nums and an integer 'k', create a boolean function that checks if there are two elements
in 'nums' such that we get 'k' when we add them together.

Example 1:
Input: nums = [4, 1, 5, -3, 6], k = 11
Output: true
Explanation: 5 + 6 is equivalent to 11

Example 2
Input: nums = [4, 1, 5, -3, 6], k = -2
Output: true
Explanation: 1 + (-3) is equivalent to -2
"""


class FindPairSum(object):
    def __int__(self):
        """Constructor."""
        pass

    @staticmethod
    def find_pair_bf(nums, k):
        """Brute force solution."""
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == k:
                    return True
        return False

    @staticmethod
    def find_pair_sorted(nums, k):
        """Sorted approach, reduces the amount of traversal needed."""
        nums.sort()
        left_idx = 0
        right_idx = len(nums) - 1

        while left_idx < right_idx:
            if nums[left_idx] + nums[right_idx] == k:
                return True
            elif nums[left_idx] + nums[right_idx] < k:
                left_idx += 1
            else:
                right_idx -= 1
        return False


if __name__ == "__main__":
    list_of_nums = [4, 1, 5, -3, 6]

    print(FindPairSum.find_pair_bf(list_of_nums, 11))  # returns True
    print(FindPairSum.find_pair_bf(list_of_nums, -4))  # returns False
    print(FindPairSum.find_pair_bf(list_of_nums, -2))  # returns True

    print(FindPairSum.find_pair_sorted(list_of_nums, 11))  # returns True
    print(FindPairSum.find_pair_sorted(list_of_nums, -4))  # returns False
    print(FindPairSum.find_pair_sorted(list_of_nums, -2))  # returns True

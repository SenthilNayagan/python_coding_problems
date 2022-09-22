"""
Problem: Remove duplicates from an integer array.

Description:
Given an array of integers nums, create a function that returns an array containing the values of
nums without duplicates; the order does not matter.

Example 1:
Input: nums = [4, 2, 5, 3, 3, 1, 2, 4, 1, 5, 5, 5, 3, 1]
Output: [4, 2, 5, 3, 1]

Example 2:
Input: nums = [1, 1, 1, 1, 1, 1, 1, 1]
Output: [1]
"""


class RemoveDuplicatesIntArray(object):
    def __init__(self):
        """Constructor."""
        pass

    @staticmethod
    def remove_duplicates_bf(nums):
        """Brute force solution.

        Time complexity: O(n^2) - Performs n iterations + Checking presence of element in output for each iteration.
        Space complexity: O(n) - Stores output in an additional array that may contain n elements in the worst case.
        """
        output = []

        for element in nums:
            if element not in output:
                output.append(element)
        return output

    @staticmethod
    def remove_duplicates_sorted(nums):
        """Sorting approach.

        Note: Take into consideration that the output that is returned will be sorted.

        Time complexity: O(n long n) - Because we sorted the array
        Space complexity: O(n)
        """
        if len(nums) == 0:
            return []

        nums.sort()
        output = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                output.append(nums[i])
        return output

    @staticmethod
    def remove_duplicates_hash(nums):
        """This solution uses hash table. Hash has the complexity of O(1) for
        both lookup and insertion.

        Time complexity: O(n) - Because we are traversing completely during worst case.
        Space complexity: O(n) - Because of the hash map.
        """
        visited = {}  # Dictionary as hash table

        for element in nums:  # This iterates n times though!
            visited[element] = True  # Overwrites the already present elements
        return list(visited.keys())


if __name__ == "__main__":
    lst_of_nums_1 = [4, 2, 5, 3, 3, 1, 2, 4, 1, 5, 5, 5, 3, 1]
    lst_of_nums_2 = [1, 1, 1, 1, 1, 1, 1, 1]

    print(RemoveDuplicatesIntArray.remove_duplicates_bf(lst_of_nums_1))  # returns [4, 2, 5, 3, 1]
    print(RemoveDuplicatesIntArray.remove_duplicates_bf(lst_of_nums_2))  # returns [1]

    print(RemoveDuplicatesIntArray.remove_duplicates_sorted(lst_of_nums_1))  # returns [4, 2, 5, 3, 1]
    print(RemoveDuplicatesIntArray.remove_duplicates_sorted(lst_of_nums_2))  # returns [1]

    print(RemoveDuplicatesIntArray.remove_duplicates_hash(lst_of_nums_1))  # returns [4, 2, 5, 3, 1]
    print(RemoveDuplicatesIntArray.remove_duplicates_hash(lst_of_nums_2))  # returns [1]
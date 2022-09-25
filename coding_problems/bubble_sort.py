"""
Bubble sort, which works by repeatedly swapping the adjacent elements if they are
in the wrong order. It's not an efficient algorithm.
"""


class BubbleSort(object):
    def __init__(self):
        """Constructor."""
        pass

    def bubble_sort_with_iteration_count(self, nums):
        """Bubble sort. It returns the iteration count as well.

        Time complexity: O(n^2)
        Space complexity: O(1) - If we are not using any temp variables such as iterations.
        """
        iterations = 0
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                iterations += 1
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]  # Swap values without the need for temp variable
        return nums, iterations


if __name__ == "__main__":
    seq1 = [5, 2, 8, 7, 3, 1, 9, 4, 6]
    seq2 = [5, 2, 3, 1]

    print(BubbleSort().bubble_sort_with_iteration_count(seq1))
    print(BubbleSort().bubble_sort_with_iteration_count(seq2))
    print(BubbleSort().bubble_sort_with_iteration_count([2, 1]))
    print(BubbleSort().bubble_sort_with_iteration_count([0]))

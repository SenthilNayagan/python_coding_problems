"""
Binary search.
"""


class BinarySearch(object):
    def __init__(self):
        """Constructor."""
        pass

    @staticmethod
    def binary_search(sequence, search_item) -> 'String':
        """
        Binary search using iteration.

        :param sequence: List of numbers.
        :param search_item: Item to be searched.
        :return: Either "Found" or "Not found".

        Time complexity: O(2^n)
        Space complexity:
        """
        sequence.sort()  # It's mandate to sort the sequence before proceed further.
        start_index = 0
        end_index = len(sequence) - 1  # Because indexing position starts at 0th position.

        while start_index <= end_index:
            mid_index = start_index + (end_index - start_index) // 2  # // is a floor division, rounding to nearest int
            mid_value = sequence[mid_index]
            if mid_value == search_item:
                return 'Found'
            elif search_item < mid_value:
                end_index = mid_index - 1
            else:
                start_index = mid_index + 1
        return 'Not found'

    @staticmethod
    def binary_search_recursive(sequence, start_index, end_index, search_item) -> 'String':
        if end_index >= start_index:
            mid_index = (end_index + start_index) // 2

            if sequence[mid_index] == search_item:
                return "Found"
            elif sequence[mid_index] > search_item:
                return BinarySearch.binary_search_recursive(sequence, start_index, mid_index - 1, search_item)
            else:
                return BinarySearch.binary_search_recursive(sequence, mid_index + 1, end_index, search_item)
        else:
            return "Not found"


if __name__ == "__main__":
    seq = [5, 2, 8, 7, 3, 1, 9, 4, 6]
    print(BinarySearch.binary_search(seq, 7))
    print(BinarySearch.binary_search(seq, 10))

    print(BinarySearch.binary_search_recursive(seq, 0, len(seq) -1, 7))
    print(BinarySearch.binary_search_recursive(seq, 0, len(seq) -1, 10))

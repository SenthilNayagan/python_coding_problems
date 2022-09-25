"""
Problem: Find first repeating character in a given string.

Description:
Given a string str, create a function that returns the first repeating character. If such
character does not exist, return the null character '\0'.

Example 1:
Input: str = “inside code”
Output: ‘i’

Example 2:
Input: str = “programming”
Output: ‘r’

Example 3:
Input: str = “abcd”
Output: ‘\0’
"""


class FindRepeatingChar(object):
    def __init__(self):
        """Constructor."""
        pass

    @staticmethod
    def first_repeating_character_bf(str):
        """Brute force approach.

        Time complexity: O(n^2)
        Space complexity: ?
        """
        for i in range(len(str)):
            for j in range(i):
                if str[i] == str[j]:
                    return str[i]
        return '\0'

    @staticmethod
    def first_repeating_character_hash(s):
        """This solution uses hash table. Hash has the complexity of O(1) for
        both lookup and insertion.

        Time complexity:
        Space complexity: O(n) - Because of hash table.
        """
        visited = {}  # Python dictionary is being used as hash table

        for c in s:
            if visited.get(c):  # O(1) for lookup
                return c
            else:
                visited[c] = True  # O(1) for insertion
        return '\0'


if __name__ == "__main__":
    print(FindRepeatingChar().first_repeating_character_bf("inside code"))  # returns 'i'
    print(FindRepeatingChar.first_repeating_character_bf("inside code"))  # returns 'i'
    print(FindRepeatingChar.first_repeating_character_bf("programming"))  # returns 'r'
    print(FindRepeatingChar.first_repeating_character_bf("abcd"))  # returns '\0'

    print(FindRepeatingChar.first_repeating_character_hash("inside code"))  # returns 'i'
    print(FindRepeatingChar.first_repeating_character_hash("programming"))  # returns 'r'
    print(FindRepeatingChar.first_repeating_character_hash("abcd"))  # returns '\0'

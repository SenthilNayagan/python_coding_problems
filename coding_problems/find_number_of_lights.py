"""
We are given a string, which consists of decimal digits (0-9).
Each digit is made of a certain number of dashes, commonly seen in LED display numbers.
For instance, 1 is made of 2 dashes, 8 is made of 7 dashes and so on.

In this seven-segment display the digits are created by, illuminating, following set of dashes:
1. 2
2. 5
3. 5
4. 4
5. 5
6. 6
7. 4
8. 7
9. 6
0. 6

Write a code that takes a string as input and returns the total number of dashes.

Input:
A string of integers

Output:
Number of dashes in the string

Sample Input:
12134

Sample Output:
18

Explanation:
1 = > 2
2 => 5
1 => 2
3 => 5
4 => 4

2 + 5 + 2 + 5 + 4 = 18
"""


class NumberOfLights(object):
    def __init__(self):
        """Constructor."""
        self.noOfLights = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 4, 8: 7, 9: 6}

    def find_no_lights(self, num):
        if num < 0:
            return 0

        total_no_lights = 0

        while num > 0:
            total_no_lights += self.noOfLights[num % 10]
            num = num // 10
        return total_no_lights


if __name__ == "__main__":
    print(NumberOfLights().find_no_lights(12134))

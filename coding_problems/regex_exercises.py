"""
Regular expression (RegEx) exercises.

^ - To check if something starts with. Example: "^Hello"
$ - To check if something ends with. Example: "World$"
[] - A set of characters. Example: "[a-m]"
\ - Signals a special sequence (can also be used to escape special characters). Example: "\d"
. - Any character (except new line character). Example: "He..o"
* - Zero or more occurrences. Example: "He*o"
+ - One or more occurrences. Example: "He.+o"
? - Zero or one occurrence. Example: "Hel?o"
{} - Exactly the specified number of occurrences. Example: "he.{2}o"
| - Either or. Example: "falls|stays"
() - Capture and group. Example: "[a-m]"

\d - String contains digits
\D - String doesn't contain digits
\s - String contains whitespace character
\S - String does not contain whitespace character
\w - String contains any word character (alpha-numeric)
\W - String does not contains any word character
\Z - Check if the specified characters are at the end of the string
"""
import re


class RegExExercises(object):
    def __init__(self):
        """Constructor."""
        self.str1 = 'an example word:cat!!'

    def sum_nums_start_with_one(self, start_num, end_num):
        """Sum all the numbers between start_num and end_num that starts with 1.

        Example:
            start_num = 1
            end_num = 20
            Numbers from 1 to 19 are eligible numbers to be summed.
        """
        sum = 0
        for e in range(start_num, end_num + 1):
            pattern = r"^[1]"
            sum += e if re.match(pattern, str(e)) else 0
        return sum


if __name__ == "__main__":
    obj = RegExExercises()
    print(obj.sum_nums_start_with_one(1, 20))

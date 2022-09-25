"""
Dictionary exercises.
"""


class DictionaryExercises(object):
    def __init__(self):
        """Constructor."""
        pass

    def sort_dict_by_value(self, dt):
        """
        Sort dictionary items by value.

        :param dt: Input dictionary.
        :return: Sorted dictionary by value.
        """
        sorted_dict = {key: value for key, value in sorted(dt.items(), key=lambda item: item[1])}
        return sorted_dict

    def sort_dict_by_key(self, dt):
        """
        Sort dictionary items by key.

        :param dt: Input dictionary.
        :return: Sorted dictionary by key.
        """
        sorted_dict = {key: value for key, value in sorted(dt.items(), key=lambda item: item[0])}
        return sorted_dict


if __name__ == "__main__":
    dt_num = {5: 4, 1: 6, 6: 3}
    dt_str = {"Apple": 4, "Banana": 6, "Pineapple": 3}
    obj = DictionaryExercises()

    print(obj.sort_dict_by_value(dt_num))
    print(obj.sort_dict_by_value(dt_str))

    print(obj.sort_dict_by_key(dt_num))
    print(obj.sort_dict_by_key(dt_str))

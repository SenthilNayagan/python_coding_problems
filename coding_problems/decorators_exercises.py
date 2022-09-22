"""
Decorators exercises.
"""


class DecoratorsExercises(object):
    def __init__(self):
        pass

    def my_decorator(func):
        def wrapper(self, *args, **kwargs):
            print("Hello", args[0])
            res = func(self, *args, **kwargs)
            print("Thanks!")
            return res
        return wrapper

    @my_decorator
    def ask_time(self, name):
        print("What's the time now?")


if __name__ == "__main__":
    DecoratorsExercises().ask_time("Ken")

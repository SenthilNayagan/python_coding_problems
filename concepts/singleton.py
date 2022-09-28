"""
Creating singleton in Python is a bit tricky.
"""


class Singleton(object):
    """Represents singleton class."""

    __instance = None

    def __init__(self):
        """Constructor."""
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            print("Creating singleton object...")
            # cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)  # One way of creating an object
            cls.__instance = object.__new__(cls, *args, **kwargs)  # Other way of creating an object.
        return cls.__instance

    def greet_msg(self, person):
        print("Hello ", person, " How you are doing?")


def main():
    """Main method."""
    obj1 = Singleton()
    obj2 = Singleton()

    obj1.greet_msg("John")
    obj2.greet_msg("Mike")


if __name__ == "__main__":
    main()

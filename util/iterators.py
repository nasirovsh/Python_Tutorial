"""
--------------------------------------------
---- Helper iterator classes, functions ----
--------------------------------------------
"""
class NextValueIterator:
    """
    A class that encapsulates an iterator and provides a method to get the next value on each call.

    Parameters:
    iterable (iterable): The iterable to be converted into an iterator.

    Methods:
    next_value() -> Any:
        Returns the next value from the iterator. Raises StopIteration if there are no more values.

    Example:
    >>> iterator = NextValueIterator([1, 2, 3])
    >>> iterator.next_value()
    1
    >>> iterator.next_value()
    2
    >>> iterator.next_value()
    3
    >>> iterator.next_value()
    Traceback (most recent call last):
        ...
    StopIteration
    """
    def __init__(self, iterable):
        """
        Initializes the NextValueIterator with an iterable.

        Parameters:
        iterable (iterable): The iterable to be converted into an iterator.
        """
        self._iterator = iter(iterable)

    def next_value(self):
        """
        Returns the next value from the iterator.

        Returns:
        Any: The next value from the iterator.

        Raises:
        StopIteration: If there are no more values in the iterator.
        """
        return next(self._iterator)


# Example usage
# if __name__ == "__main__":
#     iterator = NextValueIterator([1, 2, 3])
#     print(iterator.next_value())  # Output: 1
#     print(iterator.next_value())  # Output: 2
#     print(iterator.next_value())  # Output: 3
#     try:
#         print(iterator.next_value())  # Raises StopIteration
#     except StopIteration:
#         print("No more items.")

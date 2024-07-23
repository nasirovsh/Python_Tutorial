"""
---------------------------------------------
---- Helper decorator classes, functions ----
---------------------------------------------
"""

import time

def timeit(func):
    """ Print the time it takes for a function to run."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start
        print(f"Function {func.__name__} took {end} seconds")
        return result
    return wrapper

def print_args(func):
    """ Print the arguments a function is called with as well as its return value each time the function is called"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} arguments: {args} {kwargs} and result: {result}")
        return result
    return wrapper
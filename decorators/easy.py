# Create a timing decorator that will print the time it takes for a function to run.

import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start
        print(f"Function {func.__name__} took {end} seconds")
        return result
    return wrapper

@timeit
def add(x, y):
    return x + y

add(1, 2)

@timeit
def calculate_divisors(x):
    divisors = []
    for i in range(1, x + 1):
        if x % i == 0:
            divisors.append(i)
    return divisors

calculate_divisors(1000000)

@timeit
def calculate_prime_factors(x):
    prime_factors = []
    i = 2
    while i * i <= x:
        if x % i:
            i += 1
        else:
            x //= i
            prime_factors.append(i)
    if x > 1:
        prime_factors.append(x)
    return prime_factors

calculate_prime_factors(1000000)

# Create a decorator that will print the arguments a function is called with as well as its return value each time the function is called.

def print_args_and_return(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} arguments: {args} {kwargs} and result: {result}")
        return result
    return wrapper

@print_args_and_return
def add(x, y):
    return x + y

add(1, 2)

@print_args_and_return
def calculate_divisors(x):
    divisors = []
    for i in range(1, x + 1):
        if x % i == 0:
            divisors.append(i)
    return divisors

calculate_divisors(1000000)
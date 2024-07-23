# Python_Tutorial
Practical examples of using various Python features.

## Internal Methods

## Decorators
A function that takes another function as an argument and extends its behavior without modifying its code.

```python
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function
```

## Generators


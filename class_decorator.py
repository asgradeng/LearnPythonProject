import functools
def decorator(func):
    @functools.wraps(func)
    def inner():
        str1=func()
        return str1.upper()
    return inner
@decorator
def greet():
    return "good morning"

print(greet.__name__)
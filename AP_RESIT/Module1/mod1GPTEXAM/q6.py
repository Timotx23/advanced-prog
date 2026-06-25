from functools import wraps

def limit_calls(max_calls: int):
    """
    Decorator factory that limits how often a function may be called.
    """
    # TODO
    def wrapper1(func):
        def wrapper2(*args, **kwargs):
            nonlocal max_calls
            if max_calls > 0:
                max_calls -=1
                return func(*args, **kwargs)
            else:
                raise RuntimeError
        return wrapper2
    return wrapper1
  


@limit_calls(2)
def greet(name):
    return f"Hello {name}"


@limit_calls(1)
def square(x):
    return x * x

assert greet("Alice") == "Hello Alice"
assert greet("Bob") == "Hello Bob"

try:
    greet("Charlie")
    assert False
except RuntimeError:
    assert True

assert square(4) == 16

try:
    square(5)
    assert False
except RuntimeError:
    assert True
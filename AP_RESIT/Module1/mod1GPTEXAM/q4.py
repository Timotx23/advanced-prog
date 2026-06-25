from functools import wraps

def reject_negative(func):
    """
    Decorator that rejects negative numeric arguments.
    """
    def wrapper(*args, **kwargs):
        x = list(map(lambda s: s if s>=0 else "NO", args,))
        x2  = list(map(lambda s: kwargs[s] if kwargs[s]>=0 else "NO", kwargs,))
        if "NO" in x or "NO" in x2: raise ValueError 
        return func(*args, **kwargs)
    return wrapper
    


@reject_negative
def total_cost(price, quantity, tax=0):
    return price * quantity + tax

assert total_cost(10, 3) == 30
assert total_cost(10, 3, tax=2) == 32

try:
    total_cost(-10, 3)
    assert False
except ValueError:
    assert True

try:
    total_cost(10, 3, tax=-1)
    assert False
except ValueError:
    assert True
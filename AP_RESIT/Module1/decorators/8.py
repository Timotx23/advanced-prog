def memoize(func):
    # Write your code here
    lst = {}
    def wrapper(*args, **kwargs):
        nonlocal lst
        if args in lst.keys():
            return lst[args]
        else:
            x = func(*args, **kwargs)  
            lst[(args)] = x
            return x  
    return wrapper
   


calls = 0

@memoize
def slow_add(a, b):
    global calls
    calls += 1
    return a + b

calls = 0

assert slow_add(2, 3) == 5
assert calls == 1

assert slow_add(2, 3) == 5
assert calls == 1

assert slow_add(4, 5) == 9
assert calls == 2

assert slow_add(4, 5) == 9
assert calls == 2

print("Problem 8 passed!")
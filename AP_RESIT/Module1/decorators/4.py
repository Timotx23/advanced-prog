def count_calls(func):
    # Write your code here
    count = 0
    def inner(*args, **kwargs):
        nonlocal count 
        count += 1
        inner.call_count = count
        return func(*args, **kwargs) 
    
    inner.call_count  = count 
    return inner

@count_calls
def say_hi():
    return "hi"


@count_calls
def square(x):
    return x * x

assert say_hi.call_count == 0
assert say_hi() == "hi"
assert say_hi.call_count == 1
assert say_hi() == "hi"
assert say_hi.call_count == 2

assert square.call_count == 0
assert square(4) == 16
assert square.call_count == 1
assert square(5) == 25
assert square.call_count == 2

print("Problem 4 passed!")
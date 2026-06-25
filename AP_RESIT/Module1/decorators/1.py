def double_result(func):
    # Write your code here
    def wrapper(*args):
        x = func(*args)
        x = x*2
        return x
    return wrapper
    

@double_result
def add(a, b):
    return a + b


@double_result
def get_number():
    return 10

assert add(2, 3) == 10
assert add(-1, 5) == 8
assert get_number() == 20

print("Problem 1 passed!")
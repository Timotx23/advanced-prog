def no_negative_args(func):
    # Write your code here
    def wrapper(*args):
        for j in args:
            if j < 0:
                return "Negative numbers not allowed"
        return func(*args)
    return wrapper
 


@no_negative_args
def multiply(a, b):
    return a * b


@no_negative_args
def subtract(a, b):
    return a - b

assert multiply(3, 4) == 12
assert multiply(-3, 4) == "Negative numbers not allowed"
assert multiply(3, -4) == "Negative numbers not allowed"

assert subtract(10, 3) == 7
assert subtract(-10, 3) == "Negative numbers not allowed"

print("Problem 3 passed!")
def uppercase_result(func):
    # Write your code here
    def wrapper(*args):
        x= func(*args)
        x = x.upper()
        return x
    return wrapper
    


@uppercase_result
def greet(name):
    return f"Hello, {name}"


@uppercase_result
def whisper():
    return "please be quiet"

assert greet("Jeff") == "HELLO, JEFF"
assert whisper() == "PLEASE BE QUIET"

print("Problem 2 passed!")
def count_calls(func):
    """
    Decorator that counts how many times `func` is called.
    The wrapped function must have an integer attribute `.calls`.
    """
    def wrapper(*args, **kwargs):
        wrapper.calls+=1
        return func(*args, **kwargs)
    wrapper.calls=0
    return wrapper
    # fill in answer here
    


# Tests
@count_calls
def add(a, b):
    return a + b

print(add.calls)              # 0
print(add(1, 2))              # 3
print(add.calls)              # 1
print(add(10, -3))            # 7
print(add.calls)              # 2


@count_calls
def greet(name):
    return f"hi {name}"

print(greet("ana"))           # hi ana
print(greet("bob"))           # hi bob
print(greet.calls)            # 2


@count_calls
def no_args():
    return 42

print(no_args())              # 42
print(no_args.calls)          # 1

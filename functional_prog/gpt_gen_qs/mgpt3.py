from functools import partial
def partial_apply(func, *fixed_args, **fixed_kwargs):
    """
    Return a new function with fixed positional and keyword arguments applied.
    Later kwargs should override fixed kwargs if keys collide.
    """

    # fill in answer here
    return partial(func, *fixed_args, **fixed_kwargs)


# Tests
def operation(x, y, z):
    return x * (y + z)

doublesum = partial_apply(operation, 2)
print(doublesum(3, 1))        # 8
print(doublesum(10, -10))     # 0


def format_msg(prefix, name, suffix="!"):
    return f"{prefix}{name}{suffix}"

hi = partial_apply(format_msg, "Hi ")
print(hi("Ana"))              # Hi Ana!
print(hi("Bob", suffix=" :)"))# Hi Bob :)

kw = partial_apply(format_msg, suffix="??")
print(kw("Yo ", "Sam"))       # Yo Sam??

# Edge: override fixed kwarg
kw2 = partial_apply(format_msg, "Hello ", suffix="!")
print(kw2("Zoe", suffix="..."))  # Hello Zoe...

# Edge: mixing fixed positional args
p = partial_apply(operation, 3, 4)
print(p(5))                   # 27

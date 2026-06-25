def curry_args(*args):
    # Write your code here
    cur = args
    def inner(*args):
        nonlocal cur
        return cur+ args 
    return inner
    
  

assert curry_args(1, 2)(3, 4) == (1, 2, 3, 4)
assert curry_args("a")("b", "c") == ("a", "b", "c")
assert curry_args()(1, 2, 3) == (1, 2, 3)

print("Problem 2 passed!")
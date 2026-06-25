def add(a):
    # Write your code here
    def add_b(b):
        return a+b
    return add_b

    

assert add(2)(3) == 5
assert add(10)(-4) == 6
assert add(0)(100) == 100

print("Problem 1 passed!")
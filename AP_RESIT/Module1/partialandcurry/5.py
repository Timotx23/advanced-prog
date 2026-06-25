def curry_operation(operation):
    # Write your code here
    def inner(one):
        def inner2(two):
           return operation(one, two)
        return inner2
    return inner
    



add = curry_operation(lambda a, b: a + b)
multiply = curry_operation(lambda a, b: a * b)
power = curry_operation(lambda a, b: a ** b)

assert add(2)(3) == 5
assert multiply(4)(5) == 20
assert power(2)(3) == 8

print("Problem 1 passed!")
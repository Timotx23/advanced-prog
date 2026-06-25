def between(min_value):
    # Write your code here
    def one(maxVal):
        def two(val):
            if val <= maxVal and val >= min_value:
                return True
            return False
        return two
    return one
    
assert between(1)(10)(5) == True
assert between(1)(10)(1) == True
assert between(1)(10)(10) == True
assert between(1)(10)(11) == False
assert between(-5)(5)(0) == True
assert between(-5)(5)(-6) == False

print("Problem 5 passed!")
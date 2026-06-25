def cap_at_100(func):
    # Write your code here
    def wrapper(*args, **kwargs):
        if func(*args, **kwargs) > 100:
            return 100
        else:
            return func(*args, **kwargs)
    return wrapper
    


@cap_at_100
def add_bonus(score, bonus):
    return score + bonus


@cap_at_100
def multiply_score(score, multiplier):
    return score * multiplier

assert add_bonus(70, 20) == 90
assert add_bonus(90, 20) == 100

assert multiply_score(20, 3) == 60
assert multiply_score(60, 3) == 100

print("Problem 6 passed!")
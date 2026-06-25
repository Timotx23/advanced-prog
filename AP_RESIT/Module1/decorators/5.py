def retry_once(func):
    # Write your code here
    def wrapper(*args, **kwargs):
       try:
           return func(*args, **kwargs)
       except Exception:
           return func(*args, **kwargs)

    return wrapper
    


attempts = 0
@retry_once
def unstable_function():
    global attempts
    attempts += 1
    if attempts == 1:
        raise ValueError("Failed once")
    return "Success"
attempts = 0
assert unstable_function() == "Success"
assert attempts == 2

print("Problem 5 passed!")
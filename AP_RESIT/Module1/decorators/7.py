def require_password(func):
    # Write your code here
    def wrapper(*args, **kwargs):
        #print(kwargs)
        if kwargs["password"] != "python123":
            return "Access denied"
        return func(*args, **kwargs)
    return wrapper
    


@require_password
def view_secret(username, password=None):
    return f"Secret data for {username}"


@require_password
def delete_account(username, password=None):
    return f"Deleted account for {username}"



assert view_secret("Jeff", password="wrong") == "Access denied"
assert view_secret("Jeff", password="python123") == "Secret data for Jeff"

assert delete_account("Alex", password="nope") == "Access denied"
assert delete_account("Alex", password="python123") == "Deleted account for Alex"

print("Problem 7 passed!")
def logger(prefix):
    # Write your code here
    def inner(message):
        return f"{prefix} {message}"
    return inner
    pass

info = logger("[INFO]")
error = logger("[ERROR]")

assert info("Program started") == "[INFO] Program started"
assert info("User logged in") == "[INFO] User logged in"

assert error("File not found") == "[ERROR] File not found"

print("Problem 10 passed!")
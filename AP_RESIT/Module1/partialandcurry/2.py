def greet(greeting):
    # Write your code here
    def greet2(greats):
        return f"{greeting}, {greats}"
    return greet2
    

assert greet("Hello")("Jeff") == "Hello, Jeff"
assert greet("Hi")("Alex") == "Hi, Alex"
assert greet("Good morning")("Maria") == "Good morning, Maria"

print("Problem 3 passed!")
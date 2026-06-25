"""
LeetCode Medium: Retry Decorator

Topic:
- Decorators
- Closures
- *args and **kwargs
- Higher-order functions

Context:
You are building a small system that calls unreliable functions.
Sometimes a function fails by raising an exception.
You want to write a decorator that automatically retries the function
a fixed number of times before giving up.

Your task:
Fill in the retry_on_exception decorator.

Function to implement:

    def retry_on_exception(max_retries, allowed_exceptions):
        ...

The decorator should:
1. Return a decorator.
2. The decorator should return a wrapper.
3. The wrapper should call the original function.
4. If the original function raises one of the allowed_exceptions,
   retry it.
5. If the function succeeds, return its result immediately.
6. If the function still fails after all retries, re-raise the final exception.
7. If the function raises an exception that is NOT allowed, raise it immediately.
8. The wrapper must support *args and **kwargs.

Important:
- max_retries means the number of extra attempts after the first try.
- So max_retries = 2 means the function may be called up to 3 times total.
"""


def retry_on_exception(max_retries, allowed_exceptions):
  
    pass


# -----------------------------
# Tests
# -----------------------------

def run_tests():
    # Test 1: Function succeeds immediately
    calls = {"count": 0}

    @retry_on_exception(max_retries=3, allowed_exceptions=(ValueError,))
    def always_works(x):
        calls["count"] += 1
        return x * 2

    assert always_works(5) == 10
    assert calls["count"] == 1


    # Test 2: Function fails once, then succeeds
    calls = {"count": 0}

    @retry_on_exception(max_retries=3, allowed_exceptions=(ValueError,))
    def fails_once():
        calls["count"] += 1
        if calls["count"] == 1:
            raise ValueError("temporary failure")
        return "success"

    assert fails_once() == "success"
    assert calls["count"] == 2


    # Test 3: Function fails multiple times, then succeeds
    calls = {"count": 0}

    @retry_on_exception(max_retries=5, allowed_exceptions=(ValueError,))
    def fails_three_times():
        calls["count"] += 1
        if calls["count"] <= 3:
            raise ValueError("temporary failure")
        return "done"

    assert fails_three_times() == "done"
    assert calls["count"] == 4


    # Test 4: Function exceeds retry limit
    calls = {"count": 0}

    @retry_on_exception(max_retries=2, allowed_exceptions=(ValueError,))
    def always_fails():
        calls["count"] += 1
        raise ValueError("permanent failure")

    try:
        always_fails()
        assert False, "Expected ValueError to be raised"
    except ValueError as e:
        assert str(e) == "permanent failure"

    assert calls["count"] == 3


    # Test 5: Non-allowed exception should not be retried
    calls = {"count": 0}

    @retry_on_exception(max_retries=5, allowed_exceptions=(ValueError,))
    def raises_type_error():
        calls["count"] += 1
        raise TypeError("wrong type")

    try:
        raises_type_error()
        assert False, "Expected TypeError to be raised"
    except TypeError as e:
        assert str(e) == "wrong type"

    assert calls["count"] == 1


    # Test 6: Multiple allowed exceptions
    calls = {"count": 0}

    @retry_on_exception(max_retries=3, allowed_exceptions=(ValueError, KeyError))
    def raises_key_error_then_succeeds():
        calls["count"] += 1
        if calls["count"] == 1:
            raise KeyError("missing key")
        return "recovered"

    assert raises_key_error_then_succeeds() == "recovered"
    assert calls["count"] == 2


    # Test 7: Must support positional arguments
    calls = {"count": 0}

    @retry_on_exception(max_retries=2, allowed_exceptions=(ValueError,))
    def add(a, b):
        calls["count"] += 1
        return a + b

    assert add(3, 4) == 7
    assert calls["count"] == 1


    # Test 8: Must support keyword arguments
    calls = {"count": 0}

    @retry_on_exception(max_retries=2, allowed_exceptions=(ValueError,))
    def greet(name, punctuation="!"):
        calls["count"] += 1
        return "Hello, " + name + punctuation

    assert greet(name="Alice", punctuation="?") == "Hello, Alice?"
    assert calls["count"] == 1


    # Test 9: max_retries = 0 means only one attempt
    calls = {"count": 0}

    @retry_on_exception(max_retries=0, allowed_exceptions=(ValueError,))
    def fail_no_retry():
        calls["count"] += 1
        raise ValueError("no retry")

    try:
        fail_no_retry()
        assert False, "Expected ValueError to be raised"
    except ValueError as e:
        assert str(e) == "no retry"

    assert calls["count"] == 1


    print("All tests passed!")


run_tests()
"""
LeetCode Medium: Flexible Argument Analyzer

Topic:
- *args
- **kwargs
- working with variable positional and keyword inputs

Context:
You are building a function that receives an unknown number of inputs.
Some inputs come through *args.
Some inputs come through **kwargs.

Your task:
Fill in the function analyze_arguments.

Function behavior:
Given any number of positional arguments and keyword arguments, return a dictionary with:

1. "args_count"
   - The number of positional arguments.

2. "kwargs_count"
   - The number of keyword arguments.

3. "numeric_args_sum"
   - The sum of all positional arguments that are int or float.
   - Ignore non-numeric positional arguments.
   - Do NOT count booleans as numbers, even though bool is technically a subclass of int in Python.

4. "string_args"
   - A list of all positional arguments that are strings.
   - Keep their original order.

5. "truthy_kwargs"
   - A dictionary containing only keyword arguments whose values are truthy.
   - Keep the same key-value pairs.

6. "combined_score"
   - numeric_args_sum plus the sum of all keyword values that are int or float.
   - Again, do NOT count booleans as numbers.

Example:
analyze_arguments(1, "hi", 2.5, False, name="Alice", score=10, active=True, empty="")

Should return:
{
    "args_count": 4,
    "kwargs_count": 4,
    "numeric_args_sum": 3.5,
    "string_args": ["hi"],
    "truthy_kwargs": {"name": "Alice", "score": 10, "active": True},
    "combined_score": 13.5
}
"""


def analyze_arguments(*args, **kwargs):
   
    return_dict = {"args_count": len(args), "kwargs_count": len(kwargs.keys()), }
    return_dict["numeric_args_sum"] = sum([ i for i in args if type(i) == float or type(i) == int])
    return_dict["string_args"] = [ i for i in args if type(i) == str ]
    return_dict["truthy_kwargs"]  = {key: value for key, value in kwargs.items() if value}
    return_dict["combined_score"] = sum([ i for i in kwargs.values() if type(i) == float or type(i) == int ]) + return_dict["numeric_args_sum"]
    
    return return_dict


# -----------------------------
# Tests
# -----------------------------

def run_tests():
    # Test 1: Basic mixed input
    result = analyze_arguments(
        1,
        "hi",
        2.5,
        False,
        name="Alice",
        score=10,
        active=True,
        empty=""
    )

    assert result == {
        "args_count": 4,
        "kwargs_count": 4,
        "numeric_args_sum": 3.5,
        "string_args": ["hi"],
        "truthy_kwargs": {
            "name": "Alice",
            "score": 10,
            "active": True
        },
        "combined_score": 13.5
    }


    # Test 2: No arguments at all
    result = analyze_arguments()

    assert result == {
        "args_count": 0,
        "kwargs_count": 0,
        "numeric_args_sum": 0,
        "string_args": [],
        "truthy_kwargs": {},
        "combined_score": 0
    }


    # Test 3: Only positional numbers
    result = analyze_arguments(5, 10, -3, 2.5)

    assert result == {
        "args_count": 4,
        "kwargs_count": 0,
        "numeric_args_sum": 14.5,
        "string_args": [],
        "truthy_kwargs": {},
        "combined_score": 14.5
    }


    # Test 4: Positional strings keep original order
    result = analyze_arguments("apple", 10, "banana", False, "cherry")

    assert result == {
        "args_count": 5,
        "kwargs_count": 0,
        "numeric_args_sum": 10,
        "string_args": ["apple", "banana", "cherry"],
        "truthy_kwargs": {},
        "combined_score": 10
    }


    # Test 5: Only keyword arguments
    result = analyze_arguments(
        name="Bob",
        age=20,
        score=7.5,
        active=False,
        empty="",
        points=0
    )

    assert result == {
        "args_count": 0,
        "kwargs_count": 6,
        "numeric_args_sum": 0,
        "string_args": [],
        "truthy_kwargs": {
            "name": "Bob",
            "age": 20,
            "score": 7.5
        },
        "combined_score": 27.5
    }


    # Test 6: Booleans should not count as numbers
    result = analyze_arguments(True, False, 10, flag=True, other=False, value=5)

    assert result == {
        "args_count": 3,
        "kwargs_count": 3,
        "numeric_args_sum": 10,
        "string_args": [],
        "truthy_kwargs": {
            "flag": True,
            "value": 5
        },
        "combined_score": 15
    }


    # Test 7: Falsy values in kwargs should be excluded from truthy_kwargs
    result = analyze_arguments(
        1,
        zero=0,
        empty_string="",
        none_value=None,
        empty_list=[],
        valid_list=[1, 2],
        valid_text="hello"
    )

    assert result == {
        "args_count": 1,
        "kwargs_count": 6,
        "numeric_args_sum": 1,
        "string_args": [],
        "truthy_kwargs": {
            "valid_list": [1, 2],
            "valid_text": "hello"
        },
        "combined_score": 1
    }


    # Test 8: Mixed edge case
    result = analyze_arguments(
        -10,
        "x",
        0,
        True,
        3.5,
        label="test",
        bonus=-2,
        multiplier=0,
        enabled=True
    )

    assert result == {
        "args_count": 5,
        "kwargs_count": 4,
        "numeric_args_sum": -6.5,
        "string_args": ["x"],
        "truthy_kwargs": {
            "label": "test",
            "bonus": -2,
            "enabled": True
        },
        "combined_score": -8.5
    }

    print("All tests passed!")


run_tests()
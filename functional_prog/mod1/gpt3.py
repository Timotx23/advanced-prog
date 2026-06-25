"""
LeetCode Medium: Flexible Lambda Processor

Topic:
- *args
- **kwargs
- lambda functions
- filtering and transforming data

Context:
You are building a flexible data-processing function.
The function receives any number of positional arguments through *args.
It also receives optional behavior settings through **kwargs.

Your task:
Fill in the function process_values.

Function behavior:
process_values should accept:

    process_values(*args, **kwargs)

The positional arguments are the values you need to process.

The keyword arguments may include:

1. transform
   - A lambda/function used to transform each accepted value.
   - If not provided, use the identity function: lambda x: x

2. condition
   - A lambda/function used to decide whether a value should be accepted.
   - If not provided, accept every value.

3. combine
   - A lambda/function used to combine all transformed values into one result.
   - If not provided, return the transformed values as a list.

4. default
   - A value to return if no positional values pass the condition.
   - If not provided, use None.

Rules:
1. Only process values from args.
2. Use kwargs to get transform, condition, combine, and default.
3. First filter values using condition.
4. Then transform the accepted values using transform.
5. If no values pass the condition, return default.
6. If combine is provided, return combine(transformed_values).
7. Otherwise, return the transformed values as a list.

Example:
process_values(
    1, 2, 3, 4,
    condition=lambda x: x % 2 == 0,
    transform=lambda x: x * 10,
    combine=lambda values: sum(values)
)

Should return:
60

Explanation:
Accepted values: [2, 4]
Transformed values: [20, 40]
Combined result: 60
"""


def process_values(*args, **kwargs):
    if len(kwargs.keys()) == 0:
        return list(args)
    final = []
    for b in args:
        for i in kwargs:   
            try:
                x = kwargs[i](b)
                final.append(x)
            except:
                pass
            
    print(final)
    



# -----------------------------
# Tests
# -----------------------------

def run_tests():
    # Test 1: Basic filtering, transforming, and combining
    result = process_values(
        1, 2, 3, 4,
        condition=lambda x: x % 2 == 0,
        transform=lambda x: x * 10,
        combine=lambda values: sum(values)
    )

    assert result == 60


    # Test 2: No kwargs means return all args as a list
    result = process_values(1, 2, 3)

    assert result == [1, 2, 3]


    # Test 3: Only transform
    result = process_values(
        "a", "b", "c",
        transform=lambda x: x.upper()
    )

    assert result == ["A", "B", "C"]


    # Test 4: Only condition
    result = process_values(
        5, 10, 15, 20,
        condition=lambda x: x > 10
    )

    assert result == [15, 20]


    # Test 5: Condition filters everything, use default
    result = process_values(
        1, 3, 5,
        condition=lambda x: x % 2 == 0,
        transform=lambda x: x * 100,
        default=[]
    )

    assert result == []


    # Test 6: Combine strings
    result = process_values(
        "hello", "world", "python",
        transform=lambda x: x[0],
        combine=lambda values: "-".join(values)
    )

    assert result == "h-w-p"


    # Test 7: Combine with max
    result = process_values(
        4, 8, 2, 10,
        transform=lambda x: x * 2,
        combine=lambda values: max(values)
    )

    assert result == 20


    # Test 8: Negative numbers and condition
    result = process_values(
        -5, -2, 0, 3, 7,
        condition=lambda x: x >= 0,
        transform=lambda x: x + 1
    )

    assert result == [1, 4, 8]


    # Test 9: Empty args should return default
    result = process_values(
        condition=lambda x: True,
        transform=lambda x: x * 2,
        default="empty"
    )

    assert result == "empty"


    # Test 10: Booleans with condition
    result = process_values(
        True, False, True,
        condition=lambda x: x is True,
        transform=lambda x: "yes"
    )

    assert result == ["yes", "yes"]


    print("All tests passed!")


run_tests()
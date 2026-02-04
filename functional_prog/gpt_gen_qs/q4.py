def filtered_squares(nums, divisor, banned=set()):
    """
    Filter nums by rules and return squares of kept elements.
    """
    # TODO

    return list(filter(lambda a: a!="b",(map(lambda x:x*x if x not in banned  and x%divisor == 0 else "b",nums))))


# Tests
print(filtered_squares([1, 2, 3, 4, 5, 6], 2, banned={4}))                      # [4, 36]
print(filtered_squares([0, -2, -4, 7], 2))                                     # [0, 4, 16]
print(filtered_squares([9, 12, 15, 18], 3, banned={12, 18}))                   # [81, 225]

print(filtered_squares([], 3))                                                 # [] (edge)
print(filtered_squares([5, 10, 15], 7))                                        # [] (edge)

from collections import Counter
def rle_encode(data):
    """
    Yield (value, count) for consecutive runs in `data`.
    Must work lazily (generator).
    """
    yield(Counter(data))
    # fill in answer here
    
    
    


# Tests
print(list(rle_encode([1, 1, 2, 2, 2, 3])))        # [(1, 2), (2, 3), (3, 1)]
print(list(rle_encode("aaabbc")))                  # [('a', 3), ('b', 2), ('c', 1)]
print(list(rle_encode([True, True, False, False, True])))  # [(True, 2), (False, 2), (True, 1)]
print(list(rle_encode([5])))                      # [(5, 1)]
print(list(rle_encode([1, 2, 3])))                # [(1, 1), (2, 1), (3, 1)]

# Edge: empty input
print(list(rle_encode([])))                       # []

# Edge: works with iterators
it = iter([9, 9, 9, 8])
print(list(rle_encode(it)))                       # [(9, 3), (8, 1)]

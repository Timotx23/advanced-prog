from functools import reduce

def dedupe_by_key(items, key_fn=lambda x: x):
    """
    Return items with duplicates removed based on key_fn, keeping first occurrences.
    """
    if len(items) ==0: return []
    
    lst=[]
    for i in items:
        print("key", key_fn(i))
    #thing=(reduce(lambda acc, x: print("KEY", key_fn(x)), set(items)),0)
    #bong=reduce(lambda)
    go_through=list(map("function", items))
    return lst


# Tests
print(dedupe_by_key([1, 2, 2, 3, 1]))                                          # [1, 2, 3]
print(dedupe_by_key(["a", "A", "b"], key_fn=lambda s: s.lower()))              # ["a", "b"]
print(dedupe_by_key([("x", 1), ("y", 1), ("z", 2)], key_fn=lambda t: t[1]))    # [("x",1), ("z",2)]

print(dedupe_by_key([]))                                                       # [] (edge)
print(dedupe_by_key([0, False, 0.0], key_fn=lambda x: int(bool(x))))           # [0] (edge)

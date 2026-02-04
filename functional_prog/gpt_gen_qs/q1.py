from functools import reduce

def weighted_keyword_score(text: str, **weights) -> int:
    """
    Return the weighted keyword score of text using weights passed as kwargs.
    """
    # TODO
    pass


# Tests
print(weighted_keyword_score("Hello hello world", hello=2, world=3))          # 7
print(weighted_keyword_score("a b a c A", a=1, c=10))                         # 13
print(weighted_keyword_score("spam eggs spam spam", spam=5, eggs=2))          # 17

print(weighted_keyword_score("", a=10))                                       # 0   (edge)
print(weighted_keyword_score("No matches here", x=1, y=2, z=3))               # 0   (edge)

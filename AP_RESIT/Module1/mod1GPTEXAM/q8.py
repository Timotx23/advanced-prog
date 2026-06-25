from typing import Iterable, Optional

def first_clean_palindrome(words: Iterable[str], min_len: int) -> Optional[str]:
    """
    Return the reversed cleaned version of the first valid palindrome.

    Cleaning means:
    - lowercase
    - remove spaces

    Return None if no valid string exists.
    """
    lst = filter(
    lambda a: a != None,
    map(lambda x: x.lower().replace(" ", "") if len(x.lower().replace(" ", "")) >= min_len else None, words))

    for j in lst:
        print(j[::-1])
        if j[::-1] == j:
            
            return j[::-1]
        
    return None
        

    



assert first_clean_palindrome(
    ["abc", "Too hot to hoot", "never odd or even"],
    5
) == "toohottohoot"

assert first_clean_palindrome(
    ["hi", "abc", "A Santa at NASA"],
    10
) == "asantaatnasa"

assert first_clean_palindrome(["abc", "def"], 2) is None


def noisy():
    yield "abc"
    yield "Race car"
    raise AssertionError("Your function should stop before this point")

assert first_clean_palindrome(noisy(), 3) == "racecar"
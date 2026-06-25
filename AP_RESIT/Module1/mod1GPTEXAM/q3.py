from typing import Callable, Iterable, List, TypeVar

T = TypeVar("T")
U = TypeVar("U")

def select_items(
    items: Iterable[T],
    predicate: Callable[[T], bool],
    transform: Callable[[T], U]
) -> List[U]:
    """
    Filter and transform items using higher-order functions.
    """
    # TODO: use map/filter or comprehensions
    fil = list(filter(lambda x: x != False , list(map(lambda x: transform(x) if predicate(x) == True else False, items))))
    return fil


assert select_items(
    [1, 2, 3, 4, 5],
    lambda x: x % 2 == 1,
    lambda x: x * x
) == [1, 9, 25]

assert select_items(
    ["hi", "hello", "a", "world"],
    lambda s: len(s) >= 3,
    lambda s: s.upper()
) == ["HELLO", "WORLD"]

assert select_items([], lambda x: True, lambda x: x) == []
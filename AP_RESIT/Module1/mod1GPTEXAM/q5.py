from typing import Iterable, Iterator, Tuple, TypeVar

T = TypeVar("T")

def windows(data: Iterable[T], k: int) -> Iterator[Tuple[T, ...]]:
    """
    Lazily yield sliding windows of size k.
    """
    # TODO
    pass

assert list(windows([1, 2, 3, 4], 2)) == [(1, 2), (2, 3), (3, 4)]

assert list(windows("abcd", 3)) == [("a", "b", "c"), ("b", "c", "d")]

assert list(windows([1, 2], 3)) == []

assert list(windows([1, 2, 3], 1)) == [(1,), (2,), (3,)]

try:
    list(windows([1, 2, 3], 0))
    assert False
except ValueError:
    assert True
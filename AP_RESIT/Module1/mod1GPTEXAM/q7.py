from functools import partial
from typing import Callable

def score(base: int, multiplier: int, penalty: int, correct: int, wrong: int) -> int:
    return base + multiplier * correct - penalty * wrong


def curried_score(base: int):
    """
    Return a chain of single-argument functions until correct/wrong are needed.
    """
    
    def multiplyer(multi):
        def penalty(pen):
                make_exam = make_exam_scorer(multiplier=multi, penalty= pen )
                
        return penalty
    return multiplyer
            
    # TODO
    pass


def make_exam_scorer(multiplier: int, penalty: int) -> Callable[[int, int], int]:
    """
    Return a specialized scoring function with base fixed at 0.
    The returned function should accept correct and wrong.
    """
    # TODO
    pass

f = curried_score(10)(5)(2)
assert f(3, 1) == 23
assert f(0, 4) == 2

exam = make_exam_scorer(4, 1)
assert exam(10, 2) == 38
assert exam(5, 5) == 15

hard_exam = make_exam_scorer(10, 3)
assert hard_exam(7, 4) == 58
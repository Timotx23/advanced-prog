from typing import List, Tuple

def rank_submissions(submissions: List[Tuple[str, int, int, int]]) -> List[str]:
    """
    Return the student names in ranked order.
    """
    # TODO: use sorted with a lambda key
    # sort based on highest score
    # IF the scores are the same  sort based on the penalty
    # IF the penalty is the same sort based on time
    # If time is also the same sort based on the alphabetical order
  
        
    ranked = sorted(submissions, key=lambda i: (-i[1], i[3], i[2], i[0]))
    return [i[0] for i in ranked]
   

assert rank_submissions([
    ("Alice", 90, 40, 2),
    ("Bob", 90, 35, 2),
   ("Charlie", 95, 50, 5),
    ("Dave", 90, 35, 1),
]) == ["Charlie", "Dave", "Bob", "Alice"]

assert rank_submissions([
    ("Zoe", 80, 20, 0),
    ("Anna", 80, 20, 0),
    ("Mike", 80, 19, 1),
]) == ["Anna", "Zoe", "Mike"]

assert rank_submissions([]) == []
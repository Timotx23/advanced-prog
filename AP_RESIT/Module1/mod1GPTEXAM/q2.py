from typing import Dict, List, Tuple

def apply_updates(
    inventory: Dict[str, int],
    updates: List[Tuple[str, int]]
) -> Dict[str, int]:
    """
    Return a new inventory dictionary after applying updates.

    Do not mutate the original inventory.
    """
    # TODO
    inventory2 = {}
    for i in inventory:
        inventory2[i] = inventory[i]
    for j in updates:
        if j[0] not in inventory2.keys():
            inventory2[j[0]] = j[1]
        else:
            if inventory2[j[0]] + j[1] >=0:
                inventory2[j[0]] += j[1]
            else:
                raise ValueError

    return inventory2
    

original = {"apple": 5, "banana": 2}

result = apply_updates(original, [("apple", -2), ("orange", 4)])

assert result == {"apple": 3, "banana": 2, "orange": 4}
assert original == {"apple": 5, "banana": 2}

assert apply_updates({}, [("x", 3), ("x", -1)]) == {"x": 2}

try:
    apply_updates({"a": 1}, [("a", -2)])
    assert False
except ValueError:
    assert True
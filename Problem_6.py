def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    max_r = ints[0]
    min_r = ints[0]
    for i in range(len(ints)):
        if ints[i] > max_r:
            max_r = ints[i]
        elif ints[i] < min_r:
            min_r = ints[i]
    return min_r, max_r


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
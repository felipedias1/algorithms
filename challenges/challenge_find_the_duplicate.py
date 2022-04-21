from collections import Counter
from typing import Type


def find_duplicate(nums):
    try:
        all_nums = dict(Counter(nums))
        print(all_nums)
        duplicated = ""
        for number, quantity in all_nums.items():
            if number < 0:
                return False
            if quantity > 1:
                duplicated = number
        if not duplicated:
            return False
        return duplicated
    except(TypeError, ValueError):
        return False

from collections import Counter


def find_duplicate(nums):
    all_nums = dict(Counter(nums))
    print(all_nums)
    duplicated = ""
    for number, quantity in all_nums.items():
        if quantity > 1:
            duplicated = number
    return duplicated

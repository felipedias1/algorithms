from collections import Counter


def find_duplicate(nums):
    if check_string(nums) is False:
        return False
    all_nums = dict(Counter(nums))
    print(all_nums)
    duplicated = ""
    for key, value in all_nums.items():
        if key < 0:
            return False
        if value > 1:
            duplicated = key
    return False if not duplicated else duplicated


def check_string(list):
    for num in list:
        if type(num) == str:
            return False

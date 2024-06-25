def check_if_exist(nums: list[int]) -> bool:
    seen = set()

    for n in nums:
        if n * 2 in seen or n / 2 in seen:
            return True
        else:
            seen.add(n)

    return False


print(check_if_exist([10, 2, 5, 3]))
print(check_if_exist([7, 1, 14, 11]))

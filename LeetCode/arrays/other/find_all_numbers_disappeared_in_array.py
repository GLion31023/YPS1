def find_disappeared_numbers(nums: list[int]) -> list[int]:
    for num in nums:
        index = abs(num) - 1
        nums[index] = -abs(nums[index])

    missing_numbers = [n + 1 for n in range(len(nums)) if nums[n] > 0]

    return missing_numbers

    # unique = set(nums)
    # missing_numbers = [n for n in range(1, len(nums) + 1) if n not in unique]

    # return missing_numbers


print(find_disappeared_numbers([10, 2, 5, 10, 9, 1, 1, 4, 3, 7]))
print(find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]))

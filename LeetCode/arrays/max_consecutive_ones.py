def find_max_consecutive_ones(nums: list[int]) -> int:
    max_len = 0
    curr_streak = 0
    for n in nums:
        if n == 1:
            curr_streak += 1
        else:
            if curr_streak > max_len:
                max_len = curr_streak
            curr_streak = 0

    return max(max_len, curr_streak)


print(find_max_consecutive_ones([1, 1, 0, 1, 1, 1]))
print(find_max_consecutive_ones([1, 0, 1, 1, 0, 1]))

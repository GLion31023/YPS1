# Given an integer array nums, return the third distinct maximum number in this array.
# If the third maximum does not exist, return the maximum number.
# Input: nums = [2,2,3,1]
# Output: 1


def third_max(nums: list[int]) -> int:
    m1 = m2 = m3 = float('-inf')

    for n in nums:
        if n in {m1, m2, m3}:
            continue
        if n > m1:
            m3, m2, m1 = m2, m1, n
        elif m1 > n > m2:
            m3, m2 = m2, n
        elif m2 > n > m3:
            m3 = n

    return m3 if m3 != float('-inf') else m1


print(third_max([3, 2, 1]))
print(third_max([1, 2]))
print(third_max([2, 2, 3, 1]))
print(third_max([1, -2147483648, 2]))

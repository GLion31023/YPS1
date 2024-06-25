# Given an integer array nums, return the third distinct maximum number in this array.
# If the third maximum does not exist, return the maximum number.
# Input: nums = [2,2,3,1]
# Output: 1


def third_max(nums: list[int]) -> int:
    m1 = nums[0]
    m2 = m3 = float('-inf')

    for i in range(1, len(nums)):
        if nums[i] in {m1, m2, m3}:
            continue
        if nums[i] > m1:
            m3, m2, m1 = m2, m1, nums[i]
        elif m1 > nums[i] > m2:
            m3, m2 = m2, nums[i]
        elif m2 > nums[i] > m3:
            m3 = nums[i]

    return m3 if m3 != float('-inf') else m1


print(third_max([3, 2, 1]))
print(third_max([1, 2]))
print(third_max([2, 2, 3, 1]))
print(third_max([1, -2147483648, 2]))

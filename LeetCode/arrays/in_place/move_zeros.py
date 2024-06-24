# Given an integer array nums, move all 0's to the end of it while maintaining the order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]


def move_zeroes(nums: list[int]) -> None:
    p = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[p] = nums[i]
            p += 1

    while p < len(nums):
        nums[p] = 0
        p += 1


arr = [0, 1, 0, 3, 12]
move_zeroes(arr)
print(arr)

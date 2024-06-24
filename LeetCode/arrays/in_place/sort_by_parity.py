# Given an int array nums, move all the even integers at the beginning of the array followed by all the odd integers.
# Return any array that satisfies this condition.
# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

def sort_by_parity(nums: list[int]) -> list[int]:
    start, end = 0, len(nums) - 1

    while start <= end:
        if nums[start] % 2 > nums[end] % 2:
            nums[start], nums[end] = nums[end], nums[start]

        if nums[start] % 2 == 0:
            start += 1

        if nums[end] % 2 == 1:
            end -= 1

    return nums

    # while start <= end:
    # if nums[start] % 2 == 0:
    #     start += 1
    #     if nums[end] % 2 == 1:
    #         end -= 1
    # else:
    #     if nums[end] % 2 == 0:
    #         nums[start], nums[end] = nums[end], nums[start]
    #         start += 1
    #         end -= 1
    #     else:
    #         end -= 1
    #
    # return nums


arr = [3, 1, 2, 4]
arr1 = [0, 1]
print(sort_by_parity(arr))
print(sort_by_parity(arr1))

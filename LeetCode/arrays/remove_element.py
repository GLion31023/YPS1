# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).


def remove_element(nums: list[int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

    # i = 0
    # while i < len(nums):
    #     if nums[i] == val:
    #         nums.remove(nums[i])
    #     else:
    #         i += 1
    #
    # return len(nums)


arr = [0, 1, 2, 2, 3, 0, 4, 2]
v = 2

print(remove_element(arr, v))

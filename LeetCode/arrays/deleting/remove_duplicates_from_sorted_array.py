# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4
# respectively. It does not matter what you leave beyond the returned k (hence they are underscores).

def remove_duplicates(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0

    k = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    return k

    # k = 0
    # last = None
    # for i in range(len(nums)):
    #     if last is not None:
    #         if nums[i] == last:
    #             continue
    #         else:
    #             nums[k] = nums[i]
    #             last = nums[i]
    #             k += 1
    #     else:
    #         k += 1
    #         last = nums[i]

    # return k


arr1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
arr2 = [1, 1, 2]

print(remove_duplicates(arr1))
print(remove_duplicates(arr2))

# Fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

def duplicate_zeros(nums: list[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    n = len(nums)
    zeros = nums.count(0)
    i = n - 1

    while zeros > 0:
        if i + zeros < n:
            nums[i + zeros] = nums[i]

        if nums[i] == 0:
            zeros -= 1
            if i + zeros < n:
                nums[i + zeros] = 0

        i -= 1

    # i = 0
    #
    # while i < len(nums):
    #     if nums[i] == 0:
    #         nums.insert(i, 0)
    #         nums.pop()
    #         i += 1
    #     i += 1

    # zeros = []
    # for i, n in enumerate(nums):
    #     if n == 0:
    #         nums.pop()
    #         zeros.append((i, n))
    #
    # for i in range(len(zeros)):
    #     nums.insert(zeros[i][0] + i, 0)


arr1 = [1, 0, 2, 3, 0, 4, 5, 0]
arr2 = [1, 2, 3]

duplicate_zeros(arr1)
duplicate_zeros(arr2)

print(arr1)
print(arr2)

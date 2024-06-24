# array nums sorted in non-decreasing order -> array of the squares of each number sorted in non-decreasing order.

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

def sorted_squares(nums: list[int]) -> list[int]:
    result = [0] * len(nums)
    left, right = 0, len(nums) - 1
    add_next = len(nums) - 1

    while left <= right:
        if nums[left] * nums[left] > nums[right] * nums[right]:
            result[add_next] = (nums[left] * nums[left])
            left += 1
        else:
            result[add_next] = (nums[right] * nums[right])
            right -= 1

        add_next -= 1

    return result

    # squared_nums = [n * n for n in nums]
    # return sorted(squared_nums)


print(sorted_squares([-4, -1, 0, 3, 10]))
print(sorted_squares([-7, -3, 2, 3, 11]))

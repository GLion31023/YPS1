# array nums sorted in non-decreasing order -> array of the squares of each number sorted in non-decreasing order.

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

def sorted_squares(nums: list[int]) -> list[int]:
    squares = [0] * len(nums)
    l, r = 0, len(nums) - 1
    p = len(squares) - 1

    while l <= r:
        if nums[l] * nums[l] > nums[r] * nums[r]:
            squares[p] = nums[l] * nums[l]
            l += 1
        else:
            squares[p] = nums[r] * nums[r]
            r -= 1
        p -= 1

    return squares

    # squared_nums = [n * n for n in nums]
    # return sorted(squared_nums)


print(sorted_squares([-4, -1, 0, 3, 10]))
print(sorted_squares([-7, -3, 2, 3, 11]))

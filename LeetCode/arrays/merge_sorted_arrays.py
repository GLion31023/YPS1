# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    pm, pn = m - 1, n - 1
    p = m + n - 1

    while pn >= 0:
        if pm >= 0 and nums1[pm] > nums2[pn]:
            nums1[p] = nums1[pm]
            pm -= 1
        else:
            nums1[p] = nums2[pn]
            pn -= 1
        p -= 1


# arr1 = [1, 2, 3, 0, 0, 0]
# marr1 = 3
# arr2 = [2, 5, 6]
# narr2 = 3
#
# merge(arr1, marr1, arr2, narr2)
# print(arr1)


arr1 = [2, 0, 0, 0, 0]
marr1 = 1
arr2 = [1, 3, 4, 5]
narr2 = 4

merge(arr1, marr1, arr2, narr2)
print(arr1)

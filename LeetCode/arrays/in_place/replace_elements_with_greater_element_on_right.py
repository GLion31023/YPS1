# Given an array arr, replace every element in that array with the greatest element among the elements to its right,
# and replace the last element with -1.
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]

def replace_elements(arr: list[int]) -> list[int]:
    greatest = arr[-1]
    arr[-1] = -1
    i = len(arr) - 2

    while i >= 0:
        curr = arr[i]
        arr[i] = greatest
        if curr > greatest:
            greatest = curr

        i -= 1

    return arr


print(replace_elements([17, 18, 5, 4, 6, 1]))
print(replace_elements([400]))

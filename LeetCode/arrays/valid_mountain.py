def valid_mountain_array(arr: list[int]) -> bool:
    if len(arr) < 3:
        return False

    i = 0

    while i < len(arr) - 1 and arr[i] < arr[i + 1]:
        i += 1

    if i == 0 or i == len(arr) - 1:
        return False

    while i < len(arr) - 1 and arr[i] > arr[i + 1]:
        i += 1

    return i == (len(arr)) - 1


print(valid_mountain_array([2, 1]))
print(valid_mountain_array([3, 5, 5]))
print(valid_mountain_array([0, 3, 2, 1]))
print(valid_mountain_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

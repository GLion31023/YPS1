def height_checker(heights: list[int]) -> int:
    expected = sorted(heights)

    diff = 0

    for i in range(len(heights)):
        if heights[i] != expected[i]:
            diff += 1

    return diff


print(height_checker([1, 1, 4, 2, 1, 3]))
print(height_checker([5, 1, 2, 3, 4]))
print(height_checker([1, 2, 3, 4, 5]))

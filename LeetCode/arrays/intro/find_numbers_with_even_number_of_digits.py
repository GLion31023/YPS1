def find_numbers(nums: list[int]) -> int:
    # better performance as arithmetic faster than string operations
    def count_digits(num: int) -> int:
        digits = 0
        while num > 0:
            num //= 10
            digits += 1
        return digits

    even_numbers = 0
    for n in nums:
        if count_digits(n) % 2 == 0:
            even_numbers += 1

    return even_numbers

    # even_numbers = 0
    # for n in nums:
    #     if len(str(n)) % 2 == 0:
    #         even_numbers += 1
    #
    # return even_numbers


print(find_numbers([12, 345, 2, 6, 7896]))
print(find_numbers([555, 901, 482, 1771]))

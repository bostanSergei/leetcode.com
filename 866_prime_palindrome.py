def primePalindrome(n: int) -> int:
    def is_prime(num):
        if num <= 1:
            return False
        for d in range(2, int(num ** 0.5) + 1):
            if num % d == 0:
                return False
        return True

    while True:
        num_string = str(n)
        if num_string[::-1] == num_string and is_prime(n):
            return n

        n += 1
        if 10 ** 7 < n < 10 ** 8:
            n = 10 ** 8


# n = 85709140
# print(primePalindrome(n))

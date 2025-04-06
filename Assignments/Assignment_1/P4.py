def has_all_unique_digits(n):
    while n > 0:
        digit = n % 10
        n //= 10
        n2 = n
        while n2 > 0:
            if n2 % 10 == digit:
                return False
            n2 //= 10
    return True

N = int(input())
print(has_all_unique_digits(N))
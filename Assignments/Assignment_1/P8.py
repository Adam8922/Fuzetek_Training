def swap_first_last_digit(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev

N = int(input())
print(swap_first_last_digit(N))
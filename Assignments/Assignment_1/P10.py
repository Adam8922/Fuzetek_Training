def remove_digit(n, d):
    rem, i = 0, 0
    while n > 0:
        digit = n % 10
        if (digit != d):
            rem += digit*((10)**i)
            i += 1
        n //= 10
    return rem

N = int(input())
D = int(input())
print(remove_digit(N, D))
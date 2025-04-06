def contains_digit(n, d):
    while n > 0:
        if n % 10 == d:
            return True
        n //= 10
    return False

N = int(input())
D = int(input())
print(contains_digit(N, D))

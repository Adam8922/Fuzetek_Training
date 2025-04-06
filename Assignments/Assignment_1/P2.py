def count_specific_digit(n, d):
    count = 0
    while n > 0:
        if n % 10 == d:
            count += 1
        n //= 10
    return count

N = int(input())
D = int(input())
print(count_specific_digit(N, D))
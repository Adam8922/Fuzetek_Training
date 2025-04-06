def sum_of_digits_consecutive_powers(n):
    rev, count, sum = 0, 1, 0
    while n > 0:
        count += 1
        rev = rev * 10 + n % 10
        n //= 10
    for i in range(1, count):
        sum += (rev % 10)**i
        rev //= 10
    return sum

N = int(input())
print(sum_of_digits_consecutive_powers(N))
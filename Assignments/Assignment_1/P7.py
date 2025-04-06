def sum_even_position_digits(n):
    sum1, sum2, count = 0, 0, 0
    while n > 0:
        sum1 += n % 10
        n //= 10
        count += 1
        sum2 += n % 10
        if n > 0:
            n //= 10
            count += 1
    return sum1 if count % 2 == 0 else sum2

N = int(input())
print(sum_even_position_digits(N))
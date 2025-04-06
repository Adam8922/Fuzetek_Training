def digit_difference(n):
    Max, Min = 0, n % 10
    while n > 0:
        digit = n % 10
        if digit > Max:
            Max = digit
        if digit < Min:
            Min = digit
        n //= 10
    return Max - Min

N = int(input())
print(digit_difference(N))
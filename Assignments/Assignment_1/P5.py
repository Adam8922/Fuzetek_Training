def multiply_digits(n):
    return (n%10) * multiply_digits(n//10) if n > 0 else 1

N = int(input())
print(multiply_digits(N))
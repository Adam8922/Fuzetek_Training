def replace_digit_with_word(n):
    words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    Number = ""
    while n > 0:
        Number = words[n % 10] + Number
        n //= 10
    return Number

N = int(input())
print(replace_digit_with_word(N))
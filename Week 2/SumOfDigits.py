N = int(input("Enter number: "))

s = 0
while N > 0:
    digit = N % 10
    s += digit
    N //= 10

print("Sum of digits =", s)

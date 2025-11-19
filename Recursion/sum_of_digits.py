n = input().strip()
num = abs(int(n))
total = 0
while num > 0:
    total += num % 10
    num //= 10
print(total)


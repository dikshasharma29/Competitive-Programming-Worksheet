n = input().strip()
num = abs(int(n))
if num == 0:
    print(1)
else:
    count = 0
    while num > 0:
        num //= 10
        count += 1
    print(count)\

parts = input().split()
x = int(parts[0])
n = int(parts[1])
result = 1
i = 0
while i < n:
    result *= x
    i += 1
print(result)

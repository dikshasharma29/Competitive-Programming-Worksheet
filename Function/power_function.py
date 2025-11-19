A, B = map(int, input().split())
result = 1
i = 0

while i < B:
    result *= A
    i += 1

print(result)

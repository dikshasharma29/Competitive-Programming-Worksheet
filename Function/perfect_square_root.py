A = int(input().strip())
i = 1
found = -1

while i * i <= A:
    if i * i == A:
        found = i
        break
    i += 1

print(found)

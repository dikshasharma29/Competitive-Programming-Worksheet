N = int(input().strip())
i = N
out = []
while i >= 1:
    out.append(str(i))
    i -= 1
print(" ".join(out))

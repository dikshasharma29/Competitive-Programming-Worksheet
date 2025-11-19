s = input().rstrip("\n")
rev = []
i = len(s) - 1
while i >= 0:
    rev.append(s[i])
    i -= 1
print("".join(rev))

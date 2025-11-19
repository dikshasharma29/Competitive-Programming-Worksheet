s = input().rstrip("\n")
i = 0
j = len(s) - 1
is_pal = True
while i < j:
    if s[i] != s[j]:
        is_pal = False
        break
    i += 1
    j -= 1

if is_pal:
    print("Palindrome")
else:
    print("Not Palindrome")

A = "aeiOUz"
A = A + A
result = ""
for ch in A:
    if ch.islower():           
        if ch in "aeiou":      
            result += "#"
        else:
            result += ch
print(result)
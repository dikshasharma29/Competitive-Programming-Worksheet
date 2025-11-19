def hypotenuse(a, b): 
    s = a*a + b*b
    i = 1
    while i * i <= s:
        if i * i == s:
            return i
        i += 1
    return "Not Perfect Square"

a, b = map(int, input().split())
print(hypotenuse(a, b))

str = int(input())    
strings = []
for i in range(str):
    S = input()
    strings.append(S)
for S in strings:
    rev = ""                
    for ch in S:
        rev = ch + rev      
    if S == rev:
        print(1)
    else:
        print(0)
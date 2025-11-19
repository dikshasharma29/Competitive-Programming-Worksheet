s="String"
word=s.split()
result=""
for w in word:
    rev=""
    for ch in w:
        rev=ch+rev
    result=result+rev+" "
print(result.strip())
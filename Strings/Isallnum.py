s=input()
c=s.split()
flag=1
for ch in c:
    if not ((ch>='a' and ch<='z') or (ch>='A' and ch<='Z') or (ch>='0' and c<='9')):
        flag=0
        break
print(flag)
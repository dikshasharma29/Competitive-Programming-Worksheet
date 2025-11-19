s="abobc"
count=0
for i in range(len(s)):
    if(s[i]=='b' and s[i+1]=='o' and s[i+2]=='b'):
         count+=1
print(count)
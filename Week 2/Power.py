a = int(input("enter Base no."))
b = int(input("enter the power"))
ans = 1
for i in range(b):
    ans = ans * a
print(ans,end="")
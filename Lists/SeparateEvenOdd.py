n=list(map(int,input("Enter an Array:").split( )))
print("Odd Element")
for i in n:
    if i % 2 != 0:
        print(i, end=" ")
        
print("Even Element")
for i in n:
    if i % 2 == 0:
        print(i, end=" ")
        
        
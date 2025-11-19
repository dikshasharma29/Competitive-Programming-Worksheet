c = "Diksha Sharma"
word = c.split()          
reversed = " "             

for w in word:
    reversed = w + " " + reversed   

print(reversed.strip())
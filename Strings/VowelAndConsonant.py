T = int(input())              
strings = []                  
for i in range(T):
    S = input()
    strings.append(S)
for S in strings:
    vowel = 0
    consonant = 0
    for ch in S:
        ch = ch.lower()
        if ch.isalpha():
            if ch in "aeiou":
                vowel += 1
            else:
                consonant += 1
    print(f"{vowel} {consonant}")
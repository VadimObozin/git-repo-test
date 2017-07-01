f = open('2.txt')
s = f.read()
newS = ''
for letter in s:
    letord=ord(letter)
    if 97 <= letord <= 122:
        newS = newS + letter
    # elif 97>=letord<=122:
    #     newS = newS + letter
print(newS)
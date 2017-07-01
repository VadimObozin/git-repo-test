def letterplus2(letter):
    letter = chr(ord(letter)+2)
    return letter

#s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
s = "map"
newS = ""
for letter in s:
    newS = newS + letterplus2(letter)
print(newS)
import re
f=open('3.txt')
s=f.read()
result=re.findall(r'[^A-Z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][^A-Z]',s)
print(result)

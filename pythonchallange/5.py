import pickle

input = open('banner.p', 'rb')
obj=pickle.load(input)
print(type(obj[0]))

for lines in obj:
    line=[ch * count for ch, count in lines]
    print ("".join(line))

print(obj)
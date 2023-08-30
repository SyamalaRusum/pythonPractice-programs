#dic
d={'Ten': 10, 'Twenty': 20, 'Thirty': 30}
for i in d.keys():
    print(i,'-',d[i])

#convert 2 lists into dics
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# empty dictionary
res_dict = dict()

for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})
print(res_dict)
    #another way
res_dict = dict(zip(keys, values))
print(res_dict)

#create a dictionary by extracting the keys from a given dictionary
for i in d:
    print(i)

d=["Twenty", "Thirty"]
for keys in d:
    d.pop(keys)
print(d)
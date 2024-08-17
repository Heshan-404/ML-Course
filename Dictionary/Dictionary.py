dic = {
    'A' : 75,
    'B' : 30,
     2:'adsad',
    True : 'abc',
    (7,8) : True,
    'dic' : {'hi',3},
    'marks': [67,30]
}

print(dic)
print(dic[2])
 
print(dic['marks'][0])

# list = dic['marks']

# print(list[0])


dic['A'] = 100  #update value of key 'A'

print(dic['A'])

dic["NewKey"] = 74 # add new key value pair

dic.pop('A')        # remove key 'A'
print(dic)


print(f'dic keys : ',dic.keys(),'\n list : ',list(dic.keys()))  #


print("values : ",dic.values())

print("Items : ",dic.items())

print("type : " , type(dic.items()))

print(len(dic.values()))


dic.clear() # make this dictionary empty
del(dic)    #delete this dictionary

new_dic = {'A' : 75 , "B" : 65 , True : (34,32,432)}
for i in new_dic.keys() :
    print(f"Key : " , {i})

for i in new_dic.values() :
    print(f"Value : " , {i})
    
for i,j in new_dic.items(): 
    print(f"Key : " , {i} ," values : ",{j})
    
    
new_dic.pop('A')

print(new_dic.items())
# print(new_dic.items()[0]) TypeError: 'dict_items' object is not subscriptable

my_dict = {'a':1,'b':2,'c':3}
reversed_dict = {value : key for key,value in my_dict.items()}

print(reversed_dict) # {1: 'a', 2: 'b', 3: 'c'}

print(dict(zip("A","B")))

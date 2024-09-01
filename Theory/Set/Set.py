numbers = {1,2,3,2,2,3,1,4,5,6,7,8}

print(type(numbers))        #class<set>

print(numbers)

print(len(numbers))

print(max(numbers))
print(min(numbers))
print(sum(numbers))


numbers.remove(8)

numbers.add(10)

x = {1,2,3,2,2,3,1,4,5,6,7,8,'Dog','Cat'}
x.add(0)                # add 0 into x
x.remove('Dog')         # remove Dog from x

print(2 in numbers)     #is 2 in numbers set
print('X' , x)          
print('numbers',numbers)
x.add(2)    #add 2 into x
x.remove(3) # remove 3 from x

x.pop()
print('X' , x)    



setOne = {1,'Apple',2,'Ball',3,'Cat'}
setTwo = {1,4,5,6}


print(setOne.union(setTwo))

print(setOne | setTwo)  #get the union
print(setOne.union(setTwo))

print(setOne & setTwo)  #get the intersection
print(setOne.intersection(setTwo))


print(setOne - setTwo)  #print all elemnts in setOne but without what are in setTwo
print(setOne.difference(setTwo))
#Tupples are immutable it means we can't add remove values


name = (1,'dog',2,'Cat' , 3,3,3, 'Apple',4,6,)  #ordered collection of data and imutable (Order and elements)   used to store historical data cant be change values inside this

print(type(name))

print(name)            

print(name[2])          #print index 2 's value

print(name.index(3))    #print the first index of 4

print(name[::2])
print(name[::-1])
print(name[::-2])

num= (1,2,3,2,2,3,4,5,3,24,5,7,5,4)
# num[0] = 'ANC' we cant change values or add or remove in tupple but we can change the order
print(num , "before") 
num = num[::-1]
print(num , "reversed")
print(min(num))         #get min value

print(sorted(num))

print(name + num)


print(2 in num)
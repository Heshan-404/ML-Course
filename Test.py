a = [1, 2, 3, 4, 5, "banana", True]
print(type(a))
print(a)             # Output: [1, 2, 3, 'apple', True]

print(a[0])          # Output: 1 (accessing an element by index)
print(len(a))        # Output: 5 (finding the length of the list)

a.append("banana")   # Adding an element to the end
print(a)             # Output: [1, 2, 3, 'apple', True, 'banana']

a.remove("apple")    # Removing an element
print(a)             # Output: [1, 2, 3, True, 'banana']

print(a[2])
print(a[3])

a.pop(2)            #remove index 2 value
print(a)

print(a.pop(3))     #remove index 3 and print it

print(a.remove(2))  #remove value that it actually 2 but return none so it's printing as none

print(a.count(2))   #get count of `2`'s in the list

print(a.index(2))   #get the first index number of '2'



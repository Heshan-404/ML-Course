

# Test.py (1-39)

# Define a list
a = [1, 2, 3, 4, 5, "banana", True]

# Print the type of the list
print(type(a))

# Print the list
print(a)

# Accessing elements and their types
print(a[0])  # Accessing the first element
print(a[2])  # Accessing the third element

# List length and membership check
print(len(a))  # Length of the list
print(1 in a)  # Check if 1 is in the list

# Modifying the list
a.append("banana")  # Adding an element
a.remove("banana")  # Removing the first occurrence of "banana"
a.pop(2)  # Removing the element at index 2
a.pop(3)  # Removing the element at index 3

# Operations on the list
# print(a.count(2))  # Count of the number 2
# print(a.index(5))  # Index of the first occurrence of 5
# a.sort()  # Sort the list in ascending order
# print(sorted(a))  # Create a sorted copy of the list
# a.reverse()  # Reverse the list

# Working with another list
b = ['abdea', 'b', 'abdef', 'Abdef']

# # Finding minimum and maximum values
# print(min(b))  # Minimum value in the b list
# print(max(b))  # Maximum value in the b list

# # Combining lists
# a.extend(b)  # Add elements of b to the end of a
# print(a)
# print(a + b)  # Concatenate the lists a and b

# a.clear()   #clear the list a

# del(a)      #remove list a from memory

print(a[0:2])   #print index 0 to 2 (0,1)

print(a)
print(a[::2])   #print two by two
print(a[::-2])  #print two by two but reveresed

print(a[2::3])

print(a[4:2:-1])
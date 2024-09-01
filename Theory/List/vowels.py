questions =  ['A','a','E','e','I','i','O','o','U','u']


print(f"{questions[::2]}")
print(f"{questions[1::2]}")

print(f"{questions[::2] + questions[1::2]}")

print(f"{questions[::-2] + questions[-2::-2]}")
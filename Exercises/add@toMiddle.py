word = input("Enter your word  :  ")
length = len(word)
print(length/2)
if length%2 == 0 :
    print(word[:(length//2)]+"@"+word[(length//2)::])
else :
    # print(word[:(length//2)]+"@"+word[((length//2)+1)::])
    print(word.replace(word[(length//2)],"@")) 
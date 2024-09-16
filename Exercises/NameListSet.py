name_list = {"Amal","Kamal","Nimal"}

print(f'This is your name list : {name_list}')

inputAddOrRemove = input("Do you want to add or remove (+,-) : ")

inputName = input("Enter name : ")

if inputAddOrRemove == "+":
    if inputName in name_list:
        print(f"{inputName} is already included...")
    else:
        name_list.add(inputName)
else:
    if inputName in name_list:
       name_list.remove(inputName)
    else:
       exit(0)

print(f'This is your name list : {name_list}')
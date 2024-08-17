files = ['images','audio','video','documents','apps','system','video','images']
noDuplicatesFiles = set(files)
duplicatesCount = len(files) - len(noDuplicatesFiles)

print("Your memory is full")
if len != 0: 
    choice = input(f"There are  {duplicatesCount} duplicates found on this List , Do you want to delete files (yes/no) : ")
    if choice.lower() == 'yes':
        print(list(noDuplicatesFiles))
    else :
        print(files)
    
else:
    print("There are no duplicates found")
# email = input("Enter your email : ")
from sqlalchemy import false

email = 'heshan@yahoo.com'
tempemail = email
password = 'Heshan2002!'
if not ((email[-10:] == '@yahoo.com' or email[-10:] == '@gmail.com') and not " " in email and (email.isalnum())):
    print("invalid email")
else :
    if not password.isalnum() and len(password) > 8 and not password.islower() and not password.isupper():
        print("Done")
    else:
        print("Invalid password")




phoneNo = input("Enter Phone No :")

countryCode = input("Enter Country Code : ")

if (phoneNo[0] == '0' and len(phoneNo) == 10) and (len(countryCode) == 3):
    print(f"Phone Number with country code : {countryCode + phoneNo[1:]}")

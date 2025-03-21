username = input("Enter Username: ")
# print(username.isalpha())
if(len(username) < 12 and username.find(" ") == -1 and username.isalpha()):
    print(f"Welcome Abroad: {username}")
else:
    print(f"Your username is not validated!")
age = input("enter age: ")
idCheck = input("do ye have ID: ").lower()
if idCheck in ["true", "false"]:
    print("Entry : ", end="")
    print(f"Allowed" if int(age)>=18 and idCheck.lower() == "true" else "Rejected")
else:
    print("invalid bool input for ID")
bal = int(input("Balance : "))
wd = int(input("Withdrawl : "))
ver = input("Verified : ").lower()
if ver in ["true", "false"]:
    print("Withdrawl successful" if bal-wd>=0 and ver == "true" else "Transaction denied")
else:
    print("invalid bool input for verification status")
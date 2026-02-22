conts = {
 "Ravi": "9876543210",
 "Anita": "9123456780",
 "Rahul": "7011123456"
}

#printing contacts
print("\ncontacts:")
for k, v in conts.items():
    print(f"{k} -- {v}")

name = input("Search the name: ").lower()

flag = 0
for key, val in conts.items():
    if(key.lower()==name):
        print(f"{key}'s Phone no: ",val)
        flag = 1
        break

if not flag:
    print("Contact not found")
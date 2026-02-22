employeeDetails = []
employeeDetails.append(("c04", "ravi", "HR"))

roles = {"admin", "editor", "viewer"}

print("\nEmployees: \n"+ "".join(f"{employeeDetails[i]}\n" for i in range(len(employeeDetails))))
if "admin" in roles:
    print("Admin Access: YES")
else:
    print("Admin Access: NO")
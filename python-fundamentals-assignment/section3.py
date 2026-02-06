name = input("enter user's name: ")
age = input(f"enter {name.capitalize()}'s age: ")
status = input(f"enter {name.capitalize()}'s status: ")

print(f"User {name.capitalize()} is {int(float(age))} years old. Activity status : {bool(status)}")
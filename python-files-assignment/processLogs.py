nos = []
with open("numbers.txt", "r") as file:
    for line in file:
        nos.append(int(line.strip()))

print(f"Total Numbers: {len(nos)}")
print(f"Total Sum: {sum(nos)}")
print(f"Average : {sum(nos)/len(nos)}")

#with open("results.log")
nos = []
with open("numbers.txt", "r") as file:
    for line in file:
        nos.append(int(line.strip()))
n = len(nos)
total = sum(nos)
avg = sum(nos)/len(nos)
print(f"Total Numbers: {n}")
print(f"Total Sum: {total}")
print(f"Average : {avg}")

with open("results.log", "a") as file:
    file.write("\nFile opened successfully")
    file.write("\nData loaded : " + " ".join(f"{nos[i]}" for i in range(n)))
    file.write(f"\nTotal numbers: {total}")
    file.write(f"\nSum: {total} \nAverage = {avg}")
    file.write("\nComputation completed")
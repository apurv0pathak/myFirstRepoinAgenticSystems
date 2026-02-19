scores = [72, 90, 84, 56, 39, 45, 18, 33]

print("Scores: ", scores)
print("First 3 Student's scores : ", scores[:3])
print("Last 3 Student's scores : ", scores[len(scores)-3:])
print("Highest : ", max(scores))
print("Lowest : ", min(scores))
print("Average : ", sum(scores)/len(scores))
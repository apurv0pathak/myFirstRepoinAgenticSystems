users = []
users.append({"name":"ravi", "scores":[60, 30, 80, 30], "roles":{"viewer"}})
users.append({"name":"anita", "scores":[70, 30, 20, 100], "roles":{"editor"}})
users.append({"name":"rahul", "scores":[44, 33, 55, 81], "roles":{"admin","viewer","editor"}})

def performance(userList)-> list:
    n = len(userList)
    avgs = []
    for i in range(n):
        sum = float(0)  
        m = len(userList[i]["scores"])
        for j in range(m):
            sum+=userList[i]["scores"][j]
        sum/=m
        avgs.append(sum)
    return avgs

def accessCheck(userSet)-> bool:
    if "admin" in userSet:
        return True
    return False

def main():
    for i in range(len(users)):
        print(f"{(users[i]["name"]).capitalize()}'s average score: ", performance(users)[i])
        print(f"Admin Access: ", "Yes" if accessCheck(users[i]["roles"]) else ("No\n"))

main()
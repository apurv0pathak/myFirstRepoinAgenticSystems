def greet(name):
    name = input("Please enter your name: ")
    return print(f"Hello, {name}!")

def assess(scores: list)->tuple[int, float]:
    sum = 0
    n = len(scores)
    for i in range(n):
        sum+=scores[i]
    return n, sum/n

def pass_fail(n:float)->str:
    if n>=50:
        return "Pass"
    else:
        return "Fail"

marks = [45, 90, 64, 36, 99]

def main():
    greet("")
    print(f"Total Subjects: {assess(marks)[0]}")
    print(f"Average Score: {assess(marks)[1]}")
    print(f"Result: {pass_fail(assess(marks)[1])}")

main()
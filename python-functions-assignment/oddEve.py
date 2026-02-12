def o_e_checker(n)->bool:
    if(n%2==0):
        return True
    else:
        return False

n = int(input("Enter number: "))
print("Number is "+("Even" if o_e_checker(n) else "Odd"))
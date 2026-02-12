scores = [72, 45, 89, 30, 60]
for i in range(len(scores)):
    #print("Fail" if scores[i]<50 else "Pass")
    n = scores[i]
    if(n>=50):
        print("Pass")
    else:
        print("Fail")
    if n>100 and n<0:
        continue
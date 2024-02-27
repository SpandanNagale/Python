def Kilometer(M):
    Miles=M/1.60
    return Miles

a=float(input('enter the distance in Miles :'))
Kilometer(a)
print(f"{a} miles is :",Kilometer(a),"kilometre")
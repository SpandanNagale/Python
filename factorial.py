def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)

n = int(input("Enter the Value of n: "))  # take input from the user
print("factorial :")
for i in range(n):
   print(fact(i+1),end = " ")    
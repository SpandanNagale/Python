def fibonacci(a):
    if (a<2):
        return a
    else:
        return (fibonacci(a-2) + fibonacci(a-1))
    
n = int(input("Enter the Value of n: "))  # take input from the user
print("Fibonacci series :")
for i in range(n):
   print(fibonacci(i),end = " ")
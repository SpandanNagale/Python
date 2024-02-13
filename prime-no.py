a=int(input("enter the no.:")) #user input

for i in range(2,(a-1)):#specific condition because if else conditions
    if(a==2):#excepction
        print("The entered number is prime number")
    elif(a%i==0):#condion to check if number is composite 
        print("The entered number is composite number")
    elif(a%1==0 and a%a==0):#condion to check if number is prime
        print("The entered number is prime number")
        break

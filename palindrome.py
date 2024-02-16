class isPalindrome:
   def __init__(self): #default constructor to invoked without call
    Num=input("enter the string :")#user input
    if(Num==Num[::-1]): #to reverse string and check
      print("yes")
      print(Num)
    else:
      print("no")
      print(Num[::-1])
#driver code
a=isPalindrome()
    


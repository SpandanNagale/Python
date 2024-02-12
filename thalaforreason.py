a=input("enter string or number:")
try:
 if(len(a)==7):
    print("thala for reason")
 elif(int(a)==7):
     print("thala for reason")
 elif(int(a[0])+int(a[1])==7):
    print("thala for reason")
 elif(int(a[0])-int(a[1])==7):
    print("thala for reason")
 elif(int(a[0])+int(a[1])+int(a[2])==7):
    print("thala for reason") 
 elif(int(a[0])+int(a[1])-int(a[2])==7):
    print("thala for reason") 
 elif(int(a[0])-int(a[1])+int(a[2])==7):
    print("thala for reason")
 elif(int(a[0])-int(a[1])-int(a[2])==7):
    print("thala for reason") 
except:
   print("invalid input")
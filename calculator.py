a=int(input("enter first no:"))
b=int(input("enter second no:"))

c=input("enter operator:")
match c :

    case "+" :
        print(a+b)
    case "-" :
        print(a-b)
    case "*" :
        print(a*b)
    case "/" :
        if(a>b) :
            print(a/b)
        else:
            print(b/a)
    case _:
        print("invalid operation")
            
            
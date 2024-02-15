import random as r
#simple rock paper scissor
a=["rock,paper,scissor"]
print(a)
for i in range(3):
    b=int(input("enter your choice"))
    r.seed(3)
    c=r.randint(1,3)
    if(b==1 and c==1):          #every single condition in rock paper scissor
     print("draw")
    elif(b==1 and c==2):
     print("lose")
    elif(b==1 and c==3):
     print("win")
    elif(b==2 and c==1):
     print("win")
    elif(b==2 and c==2):
     print("draw")
    elif(b==2 and c==3):
     print("lose") 
    elif(b==3 and c==1):
     print("lose")
    elif(b==3 and c==2):
     print("win") 
    elif(b==3 and c==3):
     print("draw")


  
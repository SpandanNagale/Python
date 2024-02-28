import random

def hint():
    clues=['-a-e','r-d','y-ll-w','r-u-d']
    position=random.randint(0,len(clues)-1)
    clue=clues[position]
    return clue
def guess(clue,guess):
    if len(clue)!=len(guess):
         return False
    for i in range(len(clue)):
       if clue[i] != '-' and clue[i ]!=guess[i]:
          return False
    return True   
clue=hint()
print("your hint is :",hint())  
guesss=input("enter your guess:")
res=guess(clue,guesss) 
if res is True:
   print("you win")
else:
   print("opps you lose")       
        

import string
import random

def ran_gen(size):
    
     passw="".join([random.choice(string.ascii_letters + string.digits)
         for n in range(size)])
     return passw

password=ran_gen(5)    
print(password)
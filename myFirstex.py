# print("hello world")

import time
now= time.strftime("%H:%M:%S")
print(now)
if(00<int(time.strftime("%H"))<12):
    print("good morning")
elif(12<int(time.strftime("%H"))<15):
    print("good afternoon")
elif(15<int(time.strftime("%H"))<18):
    print("good evening")
else:
    print("good night")    

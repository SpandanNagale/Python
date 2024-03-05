import win32com.client
def voice(a):
   spandan = win32com.client.Dispatch("SAPI.SpVoice")
   for i in range(len(a)):
    spandan.Speak(a[i])

a=["rohit","ram","me","shree","aditya"]  
voice(a) 

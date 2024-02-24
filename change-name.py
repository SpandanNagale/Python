import os #importing operating system module
file=os.listdir('D:\Anime\\new\\vid') #listing no of file
print(file)

for file in file: #for loop to reach every file 
    i=1
    if (file.endswith(".mp4")): #condition to select specific file
        os.rename(f"D:\Anime\\new\\vid\{file}", f"D:\Anime\\new\\vid\{i}.mp4")#rename operation
        i=i+1
print(file)        
def sum(arr):
    add=0
    new_arr=[]
    for i in range(len(arr)):
        add=add+arr[i]
        new_arr.append(add)
    return new_arr


arr=[1,2,3,5,8,0,3,5,6]
print(sum(arr))
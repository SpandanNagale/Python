def square(list):
    s=[]
    left=0
    right=len(list)-1
    while left<=right:
        if abs(list[left])>abs(list[right]):
            s.append(list[left]**2)
            left +=1
        else:
            s.append(list[right]**2)
            right -=1
    
    return s[::-1]

a=[12,3,4,5,6,7,8,9]
print(square(a))
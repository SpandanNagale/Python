def largest_num(nums):
    large=nums[0]
    for i in range(len(nums)):
        
        if large<nums[i]:
            large=nums[i]
       
        i=i+1    
    return large


a=[1,2,3,4,5,6,87,8,7]
print(largest_num(a))
            
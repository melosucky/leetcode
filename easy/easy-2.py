# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed.
# Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
# The remaining elements of nums are not important as well as the size of nums.
# Return k.

class Solution:
    def __init__ (self, nums=[], val=int):
        num_noV=[]
        
        for i in range (len(nums)):
            if nums[i]!=val:
                num_noV.append(nums[i])
                numval=(len(nums))-len(num_noV)

        nums=[]
        for n in num_noV:
            nums.append(n)

        for e in range (numval):
            nums.append(val)
            

        k=len(num_noV)
        print(k,num_noV,nums)


nums = [3,2,2,3]
val=3
Solution(nums,val)
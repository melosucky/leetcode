# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        noDuplicate=set(nums)
        return len(noDuplicate) != len(nums)
    
solu=Solution()
nums = [3,1]
print(solu.containsDuplicate(nums))
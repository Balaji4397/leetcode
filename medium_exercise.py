#Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

#You must write an algorithm that runs in O(n) time and uses only constant extra space.

#Example 1:

#Input: nums = [4,3,2,7,8,2,3,1]
#Output: [2,3]
#Example 2:

#Input: nums = [1,1,2]
#Output: [1]

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a=set()
        result=[]
        for x in nums:
            if x not in a:
                a.add(x)
            else:
                result.append(x)
        return result
            
                
 

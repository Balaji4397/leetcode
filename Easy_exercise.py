#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

#Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

#Return k after placing the final result in the first k slots of nums.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        negative_value = []
        for x in nums:
            if x < 0:
                negative_value.append(x)
            else:
                continue
        count =0
        if len(negative_value)>0:
            for x in negative_value:
                a=abs(x)
                count = count +1
                for y in negative_value[count:]:
                    if a is abs(y):
                        negative_value.remove(y)
                    else:
                        continue
        count=0
        for x in nums:
            a=abs(x)
            count = count +1
            for y in nums[count:]:
                if a is abs(y):
                    nums.remove(y)
                else:
                    continue
        for x in nums:
            if len(negative_value)>0:
                if x in negative_value:
                    continue
                else:
                    nums.remove(x)
        return len(nums)
        
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
            
#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

#You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        count = -1
        if nums[len(nums)-1]<target:
            return len(nums)
        else:
            for x in nums:
                count +=1
                if target <= x :
                    return count   
                else:
                    continue
            
#Write a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".

#Example 1:

#Input: strs = ["flower","flow","flight"]
#Output: "fl"
#Example 2:

#Input: strs = ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings. 

class Solution:
    def longestCommonPrefix(self, strings):
        len1=len(strings)
        y=0;a=[];c=[];out=""
        while(len1>0):
            for x in range(0,len1):
                word=strings[x]
                word_len=len(word)
                if word_len>=1:
                    try:
                        a.append(word[y])
                        if x==len1-1:
                            for z in range(0,len1):
                                if word[y]==a[z]:
                                    if z==len1-1:
                                        y+=1
                                        c.append(a[z])
                                        a=[]
                                        if word_len==y:
                                            len3=len(c)
                                            for x in range(0,len3):
                                                out=out+c[x]
                                            return out
                                        else:
                                            continue
                                    else:
                                        continue
                                else:
                                    len3=len(c)
                                    for x in range(0,len3):
                                        out=out+c[x]
                                    return out
                        else:
                            continue
                    except:
                        len3=len(c)
                        for x in range(0,len3):
                            out=out+c[x]
                        return out
                else:
                    return out
        else:
            return out
            

        
                
        
            


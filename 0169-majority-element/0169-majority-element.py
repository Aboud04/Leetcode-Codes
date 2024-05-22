class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        currNum = 0
        currFreq = 1
        prevNum = nums[0]
        maxNum = prevNum
        maxFreq = currFreq
        prevMaxNum = None
        prevMaxFreq = None
        potentialMaxNum = None
        potentialMaxBool = False
        
        
        
        for i in range(1,len(nums)):
            currNum = nums[i]
            if prevNum == currNum:
                currFreq +=1
            else:
                currFreq = 1
            prevNum = currNum
            
            if potentialMaxBool and currNum == potentialMaxNum:
                prevMaxFreq = maxFreq
                prevMaxNum = maxNum
                maxNum = potentialMaxNum
                potentialMaxBool = False

            elif currFreq == maxFreq:
                potentialMaxNum = currNum
                potentialMaxBool = True
            


            if prevMaxNum and prevMaxNum == currNum and prevMaxFreq + currFreq > maxFreq:
                prevMaxNum = maxNum
                prevMaxFreq = maxFreq
                maxNum = currNum
                maxFreq = currFreq
            if maxFreq < currFreq and maxNum != currNum:
                prevMaxFreq = maxFreq
                prevMaxNum = maxNum
                maxFreq = currFreq
                maxNum = currNum
            elif maxNum == currNum:
                maxFreq += 1
            
        return maxNum

     
             
                

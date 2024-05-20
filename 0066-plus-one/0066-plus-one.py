class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[len(digits)-1] = (digits[len(digits)-1] + 1) %10
        
        for idx in range(len(digits)-1):
            if digits[len(digits)-1-idx] == 0:
                digits[len(digits)-2-idx] = (digits[len(digits)-2-idx] + 1) %10
            else:
                break


        if digits[0] == 0:
            return [1] + digits
        return digits
                
                
                
           
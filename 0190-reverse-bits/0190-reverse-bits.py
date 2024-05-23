class Solution:
    def reverseBits(self, n: int) -> int:
        string = ""
        while n > 0:
            string += str(n%2)
            n //=2
        
        while len(string) !=32:
            string+= "0"
       
        return int(string,2)
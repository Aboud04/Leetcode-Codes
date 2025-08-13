class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        x = 0
        for i in reversed(range(n)):  
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            
            if a_bit == b_bit:
                x_bit = 1 - a_bit  
                x |= (x_bit << i)
            else:
    
                x0 = x | (0 << i)
                x1 = x | (1 << i)
                prod0 = (a ^ x0) * (b ^ x0)
                prod1 = (a ^ x1) * (b ^ x1)
                
                x |= (0 << i) if prod0 >= prod1 else (1 << i)
                
        return ((a ^ x) * (b ^ x))  % 1000000007
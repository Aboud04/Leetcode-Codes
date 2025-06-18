class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        base_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        def to_base(number, base):
            result = ""
            while number:
                result += base_string[number % base]
                number //= base
            return result[::-1] or "0"
        
        for i in range(2, n - 1):
            v = to_base(n, i)
            if v != v[::-1]:
                return False
        return True
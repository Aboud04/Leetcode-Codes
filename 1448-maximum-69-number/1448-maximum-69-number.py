class Solution:
    def maximum69Number (self, num: int) -> int:
        length = len(str(num))
        mx = num
        tnum = num
        for i in range(length):
            tnum = num
            if get_digit(num, i) == 6:
                tnum = set_digit(tnum, i, 9)
            else:
                tnum = set_digit(tnum, i, 6)
            
            if tnum > mx:
                mx = tnum
        return mx

        
def get_digit(number, n):
    return number // 10**n % 10

def set_digit(num, k, new_digit):
    power = 10 ** k
    num -= (num // power % 10) * power
    num += new_digit * power
    return num
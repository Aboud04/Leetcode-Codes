class Solution:
    def reverseVowels(self, s: str) -> str:
        s= list(s)
        vowel=["a","e","i","o","u"]
        val,pos= [],[]
        for i in range(len(s)):
            if s[i].lower() in vowel:
                val.append(s[i])
                pos.append(i)
        val = val[::-1]
        for i in range(len(pos)):
            s[pos[i]] = val[i] 
        return ''.join(s)
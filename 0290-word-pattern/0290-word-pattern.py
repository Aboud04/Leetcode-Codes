class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        s = s.split()
        if len(s) != len(pattern):
            return False
        for idx,i in enumerate(pattern):
            if i not in d:
                d[i] = s[idx]
            else:
                if d[i] != s[idx]:
                    return False
        if len(d) != len(set(d.values())):
            return False
        return True
                
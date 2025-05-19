class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = 0
        mx = 0
        ss = ""
        for i in range(len(s)):
            if s[i] in ss:
                mx = max(mx,cnt)
                ss = ss[ss.find(s[i]) + 1:] + s[i]
                cnt = len(ss)
            else:
                ss = ss + s[i]
                cnt += 1
        return max(cnt,mx)
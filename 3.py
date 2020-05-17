class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            sr = set()
            for j in range(i, len(s)):
                if s[j] in sr:
                    res = max(len(sr), res)
                    break
                else:
                    sr.add(s[j])
            else:
                res = max(len(sr), res)
        return res

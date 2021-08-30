# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        
        mp = {}
        
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]], l)
            
            mp[s[r]] = r + 1
            ans = max(r - l + 1, ans)

        return ans
        
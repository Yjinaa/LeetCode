from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        cur_len = 0
        max_len = 0
        ans = []
        
        for i in range(len(s)):
            if s[i] not in ans:
                ans.append(s[i])
                cur_len = len(ans)
            else:
                idx = ans.index(s[i])
                cur_len = len(ans)
                max_len = max(cur_len, max_len)
                ans = ans[idx+1:]
                ans.append(s[i])
        
        return max(cur_len,max_len)

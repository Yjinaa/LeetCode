from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        
        seen = defaultdict(int)

        left = 0

        for right in range(len(s)):
            if s[right] not in seen:
                max_len = max(max_len, right-left+1)
            else:
                if seen[s[right]] < left:
                    max_len = max(max_len, right-left+1)
                else:
                    left = seen[s[right]] + 1
            seen[s[right]] = right
        
        return max_len


from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        sc = Counter(s)
        odd_cnt = 0
        for k in sc:
            if sc[k] % 2 != 0:
                odd_cnt += 1
        if odd_cnt == 0:
            return len(s)
        else:
            return len(s) - odd_cnt + 1

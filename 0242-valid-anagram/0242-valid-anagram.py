from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        s_char_count = defaultdict(int)
        for char in s:
            s_char_count[char] += 1
        t_char_count = defaultdict(int)
        for char in t:
            t_char_count[char] += 1
        return s_char_count == t_char_count
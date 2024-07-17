from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)

        for key in r:
            if key not in m or r[key] > m[key]:
                return False
        
        return True

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = len(nums) / 2
        nc = Counter(nums)
        for k in nc:
            if nc[k] > maj:
                return k
        
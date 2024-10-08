class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)

        left = 0
        right = len(x)-1
        while left < right:
            if x[left] == x[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
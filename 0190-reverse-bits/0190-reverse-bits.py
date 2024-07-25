class Solution:
    def reverseBits(self, n: int) -> int:
        n = str(bin(n))[2:]
        n = n.zfill(32)
        return int(n[::-1],2)
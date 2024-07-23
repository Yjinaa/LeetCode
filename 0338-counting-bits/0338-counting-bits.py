class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(n+1):
            bits = bin(i).count('1')
            answer.append(bits)
        return answer
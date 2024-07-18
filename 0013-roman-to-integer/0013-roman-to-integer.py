class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        romans = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        for i in range(len(s)-1):
            if s[i] == 'I' or s[i] == 'X' or s[i] == 'C':
                if romans[s[i+1]] > romans[s[i]]:
                    answer -= romans[s[i]]
                else:
                    answer += romans[s[i]]
            else:
                answer += romans[s[i]]

        return answer + romans[s[-1]]
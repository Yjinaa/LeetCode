class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(s) for s in strs])
        dp = [0] * min_len
        if len(strs) == 1:
            return "".join(strs)
        if  min_len == 0:
            return ""
        for i in range(min_len):
            for j in range(1,len(strs)):
                standard = strs[j-1][i]
                print(j,i,standard)
                if strs[j][i] == standard:
                    dp[i] = standard
                else:
                    return "".join(dp[:i])
        return "".join(dp[:i+1])
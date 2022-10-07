class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort(key=lambda x : x[0])
        N = len(pairs)
        dp = [1 for _ in range(N)]
        
        for index in range(1,N):
            start = pairs[index][0]
            for sub_index in range(index):
                end = pairs[sub_index][1]
                if end < start:
                    dp[index] = max(dp[index], dp[sub_index]+1)
        
        return max(dp)
                
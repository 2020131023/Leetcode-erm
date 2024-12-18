class Solution:
    def subsets(self, nums):
        def dfs(u, t):
            ans.append(t[:])
            for i in range(u, len(nums)):
                t.append(nums[i])
                dfs(i + 1, t)
                t.pop()

        ans = []
        nums.sort()
        dfs(0, [])
        return ans
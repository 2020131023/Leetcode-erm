class Solution: # iterative
    def permute(self, nums):
        res = [[]]

        if nums is None or len(nums) == 0:
            return ans

        for num in nums:
            new_res = []
            for perm in res:
                for i in range(len(perm) + 1):
                    new_perm = perm[:i] + [num] + perm[i:]
                    new_res.append(new_perm)

            res = new_res

        return res
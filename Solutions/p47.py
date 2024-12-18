class Solution:
    def permuteUnique(self, nums):
        res = [[]]
        if nums is None or len(nums) == 0:
            return res
        for num in nums:
            new_res = []
            for perm in res:
                for i in range(len(perm) + 1):
                    new_perm = perm[:i] + [num] + perm[i:]
                    if new_perm not in new_res:
                        new_res.append(new_perm)

            res = new_res

        return res
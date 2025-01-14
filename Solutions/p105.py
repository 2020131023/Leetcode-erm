class Solution:
    def buildTree(self, preorder, inorder):
        def dfs(i, j, n):
            if n <= 0:
                return None
            v = preorder[i]
            k = d[v]
            l = dfs(i + 1, j, k - j)
            r = dfs(i + 1 + k - j, k + 1, n - k + j - 1)
            return TreeNode(v, l, r)
        d = {v: i for i, v in enumerate(inorder)}
        return dfs(0, 0, len(preorder))
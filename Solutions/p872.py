class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(root):
            if root is None:
                return []
            ans = dfs(root.left) + dfs(root.right)
            return ans or [root.val]

        return dfs(root1) == dfs(root2)
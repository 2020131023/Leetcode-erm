class Solution(object):
    def preorderTraversal(self, root):
        if not root:
        	return []

        stack, result = [root], []
        while stack:
        	element = stack.pop()
        	result.append(element.val)

        	if element.right:
        		stack.append(element.right)
        	if element.left:
        		stack.append(element.left)

        return result
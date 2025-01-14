class Solution(object):
    def simplifyPath(self, path):
        result = "/"
        stack = []
        index = 0
        while index < len(path):
        	if path[index] == '/':
        		index += 1
        		continue
        	curr_str = ""
        	while index < len(path) and path[index] != '/':
        		curr_str += path[index]
        		index += 1
        	if curr_str == '.' or curr_str == "":
        		index += 1
        		continue
        	elif curr_str == "..":
        		if stack:
	        		stack.pop()
        		index += 1
        	else:
        		stack.append(curr_str)
        		index += 1

        for index in range(len(stack)):
        	if index != len(stack) -1:
        		result += stack[index] + '/'
        	else:
        		result += stack[index]
        return result
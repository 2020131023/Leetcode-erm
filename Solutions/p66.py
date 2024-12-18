class Solution(object):
    def plusOne(self, digits):
        result = []
        if not digits:
        	return []

        carry = 1
        new_digits = digits[::-1]

        for index in range(len(new_digits)):
        	new_digits[index], carry = (new_digits[index] + carry)%10, (new_digits[index] + carry)/10

        if carry > 0:
        	new_digits.append(carry)
        return new_digits[::-1]
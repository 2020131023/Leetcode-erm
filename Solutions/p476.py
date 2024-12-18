class Solution:
    def findComplement(self, num):
        return num ^ (2 ** (len(bin(num)[2:])) - 1)
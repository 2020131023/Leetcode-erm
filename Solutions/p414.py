class Solution:
    def thirdMax(self, nums):
        m1 = m2 = m3 = float("-inf")
        for num in nums:
            if num in [m1, m2, m3]:
                continue
            if num > m1:
                m3, m2, m1 = m2, m1, num
            elif num > m2:
                m3, m2 = m2, num
            elif num > m3:
                m3 = num
        return m3 if m3 != float("-inf") else m1
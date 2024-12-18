class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        ans = 0
        i, j = 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            ans += 1
        return ans
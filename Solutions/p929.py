class Solution:
    def numUniqueEmails(self, emails):
        s = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '')
            i = local.find('+')
            if i != -1:
                local = local[:i]
            s.add(local + '@' + domain)
        return len(s)
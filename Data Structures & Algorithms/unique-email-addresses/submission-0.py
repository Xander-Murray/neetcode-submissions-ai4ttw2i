class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = {}

        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
        
            final = local + '@' + domain
            unique[final] = unique.get(final, 0) + 1
        


        return len(unique)
            
        
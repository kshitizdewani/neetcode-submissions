class Solution:
    @staticmethod
    def get_clean_email(local, domain):
        local = local.split('+')[0].replace('.','')
        return f'{local}@{domain}'

    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        
        for mail in emails:
            local_name, domain_name = mail.split("@")
            cleaned_email = self.get_clean_email(local_name, domain_name)
            if cleaned_email not in email_set:
                email_set.add(cleaned_email)
            else:
                pass
        
        return len(email_set)

         
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emails_set = set()
        for email in emails:
            local, domain = email.split("@")
            curr_email = []
            for char in local:
                if char == ".":
                    continue
                if char == "+":
                    break
                curr_email.append(char)
            emails_set.add("".join(curr_email) + "@" + domain)
        return len(emails_set)

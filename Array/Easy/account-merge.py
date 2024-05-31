#User function Template for python3
class Solution:
    def accountsMerge(self, accounts):
        # Code here
        from collections import defaultdict
        
        parent = {}
        email_to_name = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX
        
        # Step 1: Initialize Union-Find structure
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                union(first_email, email)
                email_to_name[email] = name
        
        # Step 2: Aggregate emails by their root
        email_to_root = defaultdict(list)
        for email in parent:
            root_email = find(email)
            email_to_root[root_email].append(email)
        
        # Step 3: Construct the result
        result = []
        for root_email, emails in email_to_root.items():
            name = email_to_name[root_email]
            result.append([name] + sorted(emails))
        
        return result

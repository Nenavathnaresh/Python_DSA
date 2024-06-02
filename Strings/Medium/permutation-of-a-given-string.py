def find_permutation(S):
    def backtrack(path, used):
        if len(path) == len(S):
            perm_set.add(''.join(path))
            return
        for i in range(len(S)):
            if used[i]:
                continue
            if i > 0 and S[i] == S[i-1] and not used[i-1]:
                continue
            used[i] = True
            path.append(S[i])
            backtrack(path, used)
            path.pop()
            used[i] = False

    perm_set = set()
    S = sorted(S)
    used = [False] * len(S)
    backtrack([], used)
    
    return sorted(list(perm_set))

# Example usage:
print(find_permutation("ABC"))  # Output: ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
print(find_permutation("ABSG"))  # Output: ['ABGS', 'ABSG', 'AGBS', 'AGSB', 'ASBG', 'ASGB', 'BAGS', 'BASG', 'BGAS', 'BGSA', 'BSAG', 'BSGA', 'GABS', 'GASB', 'GBAS', 'GBSA', 'GSAB', 'GSBA', 'SABG', 'SAGB', 'SBAG', 'SBGA', 'SGAB', 'SGBA']

def compute_z_array(s):
    n = len(s)
    z = [0] * n
    left = right = 0
    for i in range(1, n):
        if i <= right:
            z[i] = min(right - i + 1, z[i - left])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > right:
            left, right = i, i + z[i] - 1
    return z

def z_algorithm(text, pattern):
    concat = pattern + "$" + text
    z_array = compute_z_array(concat)
    pattern_length = len(pattern)
    matches = []
    for i in range(pattern_length + 1, len(concat)):
        if z_array[i] == pattern_length:
            matches.append(i - pattern_length - 1)
    return matches

def compute_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k - 1]
        if pattern[k] == pattern[q]:
            k += 1
        pi[q] = k
    return pi

def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    pi = compute_prefix_function(pattern)
    q = 0
    matches = []
    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]
        if pattern[q] == text[i]:
            q += 1
        if q == m:
            matches.append(i - m + 1)
            q = pi[q - 1]
    return matches

# Example usage
if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    
    print("KMP Algorithm:")
    print("Pattern found at positions:", kmp(text, pattern))
    
    print("\nZ Algorithm:")
    print("Pattern found at positions:", z_algorithm(text, pattern))

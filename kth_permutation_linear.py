from math import factorial

def kth_permutation_fast(elements, k):
    n = len(elements)
    k %= factorial(n)
    factorials = [factorial(i) for i in range(n)]
    # elements = sorted(elements)
    used = [False] * n
    permutation = []

    for i in range(n):
        fact = factorials[n - 1 - i]
        index = k // fact
        k %= fact
        
        count = -1
        for j in range(n):
            if not used[j]:
                count += 1
            if count == index:
                permutation.append(elements[j])
                used[j] = True
                break

    return permutation
import time
n = 16
# Example Usage
elements = [i for i in range(n)]
k = 1  # 0-based index
s1 = time.time()
kth_permutation_fast(elements, k)  # Output: [1, 3, 2, 4]
s2 = time.time()

print(s2-s1)

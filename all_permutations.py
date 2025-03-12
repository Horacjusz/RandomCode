def all_permutations_from(perm):
    """
    Takes a starting permutation and generates all permutations in lexicographical order,
    cycling back to the starting permutation.
    """
    # Convert the input to a list if not already
    perm = perm[:]
    start_perm = perm[:]
    is_first_iteration = True

    while is_first_iteration or perm != start_perm:
        yield perm[:]
        perm = next_permutation_from_list(perm)
        if perm is None:  # If the permutation reaches the last one, restart from the smallest
            perm = sorted(start_perm)  # Use the same order as the first time
        is_first_iteration = False


def next_permutation_from_list(perm):
    """
    Takes a permutation and returns the next lexicographical permutation.
    If the input is the last permutation, return None.
    """
    # Convert the list into indices
    perm = perm[:]  # Make a copy to avoid modifying the original list
    n = len(perm)

    # Step 1: Find the largest index i such that perm[i] < perm[i + 1]
    i = n - 2
    while i >= 0 and perm[i] >= perm[i + 1]:
        i -= 1

    if i == -1:  # If no such i exists, this is the last permutation
        return None

    # Step 2: Find the largest index j such that perm[j] > perm[i]
    j = n - 1
    while perm[j] <= perm[i]:
        j -= 1

    # Step 3: Swap perm[i] and perm[j]
    perm[i], perm[j] = perm[j], perm[i]

    # Step 4: Reverse the subarray perm[i + 1:]
    perm[i + 1:] = reversed(perm[i + 1:])

    return perm
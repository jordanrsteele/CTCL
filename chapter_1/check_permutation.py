from collections import Counter

def check_permutation(string1, string2):

    counter = Counter()
    for c in string1:
        counter[c] += 1

    for c in string2:
        counter[c] -= 1

    for val in counter:
        if counter[val] != 0:
            return False

    return True

s1 = 'asdfghjkl'
s2 = 'lkjhgfdsa'
print(check_permutation(s1, s2))

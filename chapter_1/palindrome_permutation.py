from collections import Counter

# returns all possible permutations of a string
def palindrome_permutation(myString):
    counter = Counter()
    for c in myString:
        counter[c] += 1

    start = 0
    end = 1
    s = []
    for key in counter:
        if counter[key] >= 2:
            s.insert(start, key)
            s.insert(len(s) - start, key)
            start += 1

    newString = ''
    newString = newString.join(s)
    print(newString)

    if len(newString) > 2:
        return True, newString

s = 'tact coa'
print(palindrome_permutation(s))

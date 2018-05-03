

# returns a string with whiteplace replaced with '%20'
def url_ify(myString, strlen):
    myString = myString[:13]
    newString = myString.replace(" ", "%20")
    return newString

s1 = 'Mr John Smith      '
print(url_ify(s1, 13))

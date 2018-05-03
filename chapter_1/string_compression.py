
# simple string compression alg using tail recursion
def string_compression(myString, finalStr, count):

    if myString == None or len(myString) < 2:
        finalStr += myString[0]
        finalStr += str(count)
        return finalStr

    if myString[0] != myString[1]:
        finalStr += myString[0]
        finalStr += str(count)
        count = 1
    else:
        count += 1

    # remove first element from list before returning
    return string_compression(myString[1:], finalStr, count)


def string_comp_helper(str):
    compressed_string = string_compression(str, "", 1)

    if len(compressed_string) > len(str):
        return str

    return compressed_string

str = string_comp_helper("aabbaaaaaaa")
print(str)



def one_way(str1, str2):
    if str1 == str2:
        return True

    # check for insert a char

    for i in range(0, len(str1)):
        for j in range(0, len(str2) + 1):
            newString = list(str2)
            newString.insert(j, str1[i])
            if "".join(newString) == str1:
                return True


    # check for remove a char
    for i in range(0, len(str1)):
        for j in range(0, len(str2)):
            newString = list(str1)
            newString[j] = ""

            newString = "".join(newString)
            if newString == str2:
                return True


    # check for replace char
    for i in range(0, len(str1)):
        for j in range(0, len(str2)):
            newString = list(str1)
            newString[i] = str2[j]

            newString = "".join(newString)
            if newString == str2:
                return True

    return False

print(one_way("ake", "ale"))

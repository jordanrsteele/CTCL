
# returns true if string is unique, else false
def is_unique(myString):

    for i in range(int(len(myString)/2)):
        if(myString[i]) == myString[len(myString) - 1 - i]:
            print('false')
            exit(0)
    print("true")


myString = 'asasadkalsjf'

is_unique(myString)

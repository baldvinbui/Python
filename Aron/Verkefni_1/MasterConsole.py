from random import randint  # Get Random

# Checks if numbers match the generated numbers from computer.
def numInList(computerList, userList):
    num = 0
    for a in xrange(0, len(computerList)):
        if computerList[a] in userList:
            num = num + 1
    return num


# Checks if numbers are in correct place.
def numInPlace(computerList, userList):
    num = 0
    for x in xrange(0, len(computerList)):
        if computerList[x] == userList[x]:
            num = num + 1
    return num

# Computer gets 5 random numbers
computerList = [randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9)]
userList = []   # List to save user inputs

while True:
    for x in xrange(1, 6):
        userList.append(input("Select number " + str(x) + " "))

    if numInPlace(computerList, userList) == 5:
        print "You Win!"
        break

    print str(numInList(computerList, userList)) + " Numbers are correct but in wrong place"

    print str(numInPlace(computerList, userList)) + " Numbers are in correct place"
    break

names = ["Man City", "Man United", "Liverpool", "Chelsea", "Tottenham", "Arsenal"]

def createInitialMatchups(labels):
    matchups = [[], []]
    for i in range(int(len(labels) / 2)):
        matchups[0].append(i)
        matchups[1].append(len(labels) - 1 - i)
    return matchups

def rotateMatchups(matchups):
    rowOneEnd = matchups[0].pop(len(matchups[0])-1)
    rowTwoFront = matchups[1].pop(0)
    matchups[1].append(rowOneEnd)
    matchups[0].insert(1, rowTwoFront)

def printMatchups(matchups, labels):
    for i in range(len(matchups[0])):
        print(f"{labels[matchups[0][i]]} - {labels[matchups[1][i]]}")
    print("\n")

def generateEven(labels):
    rounds = len(labels) - 1
    matchups = createInitialMatchups(labels)
    for i in range(rounds):
        print(f"Week {i+1}")
        printMatchups(matchups, labels)
        rotateMatchups(matchups)

def generateOdd(labels):
    labelsTemp = [label for label in labels]
    labelsTemp.insert(0, "Bye")
    generateEven(labelsTemp)

def generate(labels):
    if len(labels)%2 == 0:
        generateEven(labels)
    else:
        generateOdd(labels)

generate(names)
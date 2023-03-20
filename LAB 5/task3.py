inputFile = open('input3.txt').read().splitlines()
outFile = open('output3.txt', 'w+')
taskCount = int(inputFile[0])
taskList = []
callList = []
for i in inputFile[1]:
    if i != " ":
        taskList.append(int(i))
for i in inputFile[2]:
    callList.append(i)
taskList = sorted(taskList)


def jackJill(taskList, callList):
    jackCount = 0
    jackList = []
    jillCount = 0
    sequence = ""
    for i in callList:
        if i == "J":
            m = taskList.pop(0)
            jackCount += m
            jackList.append(m)
            sequence += str(m)
        elif i == 'j':
            k = jackList.pop()
            jillCount += k
            sequence += str(k)
    #print(sequence)
    outFile.write(f"{sequence}\n")
    #print(f"Jack will work for {jackCount} hours\nJill will work for {jillCount} hours")
    outFile.write(f"Jack will work for {jackCount} hours\nJill will work for {jillCount} hours")


jackJill(taskList, callList)

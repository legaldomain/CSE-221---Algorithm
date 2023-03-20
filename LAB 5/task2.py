inputFile = open('input2.txt').read().splitlines()
outFile = open('output2.txt', 'w+')


def Assignment_Selection(arr, n, m):
    count = 0
    sortArr = sorted(arr)
    myDict = {}
    done = []
    for i in range(1, m + 1):
        myDict[i] = []
    for i in range(m):
        done.append([sortArr[i][0], sortArr[i][1]])
        myDict[i + 1].append([sortArr[i][1], sortArr[i][0]])
        count += 1

    for j in range(m, n):
        for k in range(m):
            start = sortArr[j][1]
            finish = done[k][0]
            if start >= finish:
                done[k] = sortArr[j]
                myDict[k + 1].append([sortArr[j][1], sortArr[j][0]])
                count += 1
                break

    #print(f"Task done by each people: {myDict}")
    #print("Total:", count)
    outFile.write(str(count))
n = int(inputFile[0].split()[0])
m = int(inputFile[0].split()[1])

myList = []
for i, j in enumerate(inputFile):
    if i != 0:
        x = j.split()
        myList.append([int(x[1]), int(x[0])])
Assignment_Selection(myList, n, m)

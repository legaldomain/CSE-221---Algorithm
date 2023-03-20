inputFile = open('input1.txt').read().splitlines()
outFile = open('output1.txt', 'w+')

def Assignment_Selection(arr, n):
    sortArr = sorted(arr)
    output = []
    count = 1
    finish = sortArr[0][0]

    output.append([sortArr[0][1], sortArr[0][0]])
    for i in range(1, len(sortArr)):
        startTime = sortArr[i][1]
        if startTime >= finish:
            count += 1
            finish = sortArr[i][0]
            output.append([sortArr[i][1], sortArr[i][0]])


    #print(count)
    outFile.write(f'{count}\n')
    for j in output:
        #print(j[0], j[1])
        outFile.write(f'{j[0]} {j[1]}\n')



n = int(inputFile[0])
myList = []

for i, j in enumerate(inputFile):
    if i != 0:
        x = j.split()
        myList.append([int(x[1]), int(x[0])])

Assignment_Selection(myList, n)
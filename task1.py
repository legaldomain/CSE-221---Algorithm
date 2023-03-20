f = open("input1.txt","r")
f1 = open("output1.txt","w")

n = int(f.read())

def minDP(n):
    if not n>= 0 and n<=999:
        return - 1

    arr = [10**9 for i in range(n+1)]

    arr[0]= 0

    for i in range(n+1): #nested loop
        for j in str(i):
            arr[i] = min(arr[i],arr[i-int(j)] + 1)

    return arr[n]

final = minDP(n)
print(final)
f1.write("Minimum Number of steps:")
f1.write(str(final))
f.close()
f1.close()
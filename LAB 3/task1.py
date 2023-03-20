input_file = open("input1.txt",'r').read().splitlines()
def graph(arr):
    mydict = {}

    for i in range(1,len(arr)):
        x = arr[i].split()
        key = int(x[0])
        for j in range(len(x)):
            if key not in mydict.keys():
                if int(x[j]) == key and len(x) == 1:
                    mydict[key] = []

                else:
                    if int(x[j]) != key:
                        mydict[key] = [int(x[j])]

            else:
                mydict[key].append(int(x[j]))

    return mydict

mydict = graph(input_file)
print(f"adjacent list is:{mydict}")
output1 = open("output1.txt","w+")
output1.write(f'adjacent list: {mydict}\n')


for key,value in mydict.items():
    if len(value) == 0:
        output1.write(f"{key}\n")
        print(f"{key}")
    else:
        output1.write(f"{key}->")
        print(f"{key} -> ", end=" ")
        for i, j in enumerate(value): #builtin enumerate
            if i == len(value) - 1:
                output1.write(f"[{j}]\n")
                print(f"[{j}]")
            else:
                output1.write(f"[{j}] -> ")
                print(f"[{j}] -> ", end=" ")







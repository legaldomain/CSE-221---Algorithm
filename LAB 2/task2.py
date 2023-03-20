#TASK 2

def selectionSort(arr, pas, count):
    for i in range(count): #whole array traversed
        temp = 0 #to store the sorted array part
        min = arr[-1] #sorting from the last index
        for j in range(i, pas):
            if arr[j] <= min:
                min = arr[j]
                temp = j #sorted min value array stored here
        arr[i], arr[temp] = arr[temp], arr[i]
    return arr


file2 = open("input2.txt", 'r').read().splitlines()
pas = int(file2[0].split()[0])
count = int(file2[0].split()[1])
array = file2[1].split()
form_arr = []


for i in array:
    form_arr.append(int(i))
print(f"given arr: {form_arr}")

func_call = selectionSort(form_arr, pas, count)
print(f"sort arr by preference:", end=" ")
output2 = open("output2.txt", 'w+')
for i in range(count):
    print(func_call[i], end=" ")
    output2.write(f"{str(func_call[i])} ")
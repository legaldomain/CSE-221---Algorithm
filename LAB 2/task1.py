def bubblesort(arr):
  for i in range(len(arr)-1):
    flag = False

    for j in range(len(arr)-1):
      if arr[j] > arr[j+1]:
        #swapping
        arr[j+1], arr[j] = arr[j] , arr[j + 1]
        flag = True

    if flag == False:
      break
  return arr

 
file1 = open ("input1.txt","r")
inp_file = file1.read().split(' ')
inp_file = [int(i) for i in inp_file]
print(inp_file[1::])
temp = bubblesort(inp_file[1::])
print(temp)

x = ""
for i in temp:
  x+= str(i) + " "

output = open("output1.txt","w")
output.write(x)
output.close()

#Complexity : generally bubble sort complexity is θ(n2). The best case θ(n)
#happens when the given array is already sorted, then the 1st loop will execute 1 time.
#when i = 0 the inner loop run and check if any value bigger than prev one
#when arr is already sorted flag will be false which will execute the 1st loop 1 time only & thus the best casecomplexity will be theta(n) 





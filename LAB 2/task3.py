#TASK 3

def insertationsort(arr1,arr2,new):
  i = 1 #staring pointer 1
  while i < new:
    j = i - 1 #pointer 2 always before pointer 1

    while j >= 0:
      if int(arr1[j]) < int(arr1[j+1]):
        #we will do 2 swaps as 2 arrays
        arr1[j] , arr1[j+1] = arr1[j+1], arr1[j]
        arr2[j], arr2[j+1] = arr2[j+1], arr2[j]

      else:
        break
      
      j -= 1
    
    i+=1

  return arr2

file3 = open("input3.txt","r").read().splitlines()
new = int(file3[0])
id_list = file3[1].split()
mark_list = file3[2].split()


func_call3 = insertationsort(mark_list,id_list,new)
output = open("output3.txt","w+")
for i in func_call3:
  print(i, end= " ")
  output.write(f"{i}")


  




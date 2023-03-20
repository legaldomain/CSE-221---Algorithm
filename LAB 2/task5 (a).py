#TASK 5

import time

def partition(A,p,q):
  piv = A[p] #leftmost element as pivot
  i = p
  for j in range(p+1, q+1): 
    if A[j] <= piv:
      i = i+1
      A[i], A[j] = A[j] , A[i]

  A[p], A[i] = A[i], A[p]
  return i 

def quicksort(A,p,r):
  if p< r:
    q  = partition(A,p,r)
    quicksort(A,p,q-1)
    quicksort(A,q+1,r)

  return A


start  = time.time()
file5 = open("input5a.txt","r")
infile5 = file5.read().split()

unsort = " "
for i in infile5:
  unsort+=i + " "

print("given arr:",unsort)


infile5 = [int(i) for i in infile5]
sorted_arr = quicksort(infile5, 0 ,len(infile5)-1)

st= " "
for i in range(len(sorted_arr)):
  st+= str(sorted_arr[i]) + " "

unsort = "given arr:" + unsort
st = "sorted arr:" + st
end = "time taken:" + str(time.time())

output5 = open("output5a.txt","w")
output5.write(unsort)
output5.write(st)
output5.write(end)
print(st)
output5.close()








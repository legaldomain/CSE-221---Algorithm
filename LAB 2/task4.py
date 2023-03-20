#TASK 4
file4 = open("input4.txt","r")
output4 = open("output4.txt","w")
s = file4.read()
ifile = s.splitlines()
N = int(ifile[0])
A = ifile[1].split(" ")
A = [int(i) for i in A]



def merge (A,p,q,r):
  n1 = q-p+1
  n2 = r-q
#p = FIRST, q = MIDDLE , r = LAST
  #2 temp array for storing 2 sub arrays

  L = [0] * n1
  R = [0] * n2

  #Copy data to temp arrays L[] and R[]
  for i in range(0,n1):
    L[i] = A[p+i]

  for j in range(0,n2):
    R[j] = A[q+1+j]

  f = 0  # Initial index of first subarray
  g = 0 # Initial index of second subarray
  h = p  # Initial index of merged subarray
  #merging condition
  while f< n1 and g <n2: #f index will always be smaller than len(list)

    if L[f] <= R[g]:
      A[h] = L[f] #element merged to the new sub array
      f+=1 

    else:
      A[h] = R[g]
      g+=1
    h+=1
  #check any value left in LEFT SUBLIST
  while f < n1:
    A[h] = L[f]
    f+=1
    h+=1
  #check any value left in RIGHT SUBLIST
  while g<n2:
    A[h] = R[g]
    g+= 1
    h+=1

def mergesort(A,p,r):
  if p < r:
    q = p+(r-p)//2
    mergesort(A,p,q)
    mergesort(A,q+1,r)
    merge(A,p,q,r)

  return A

output4.write("merged arr: \n")

if N ==len(A):
  Final = mergesort(A,0,N-1)
  final_output = " "
  for h in Final:
    final_output = final_output + str(h) + " "

  output4.write(final_output)

else:
  output4.write("raised error!")

print(final_output)
file4.close()
output4.close()













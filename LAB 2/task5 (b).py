
#partition part fron 5a
def partition(A,p,q):
    x=A[p]
    i=p
    for j in range(p+1,q+1):
        if A[j]<=x:
            i=i+1
            A[i],A[j]=A[j],A[i]
    A[p],A[i]=A[i],A[p]
    return i

def find_k(A,p,r,k):
    if p == r:
        if p == k:
    
            return A[p]
        else:
            return
    else:
        q = partition(A,p,r)
        if q == k:
            return A[q]
        elif q<k:
            return find_k(A,q+1,r,k)
        else:
            return find_k(A,p,q-1,k)


file=open("input5b.txt", mode="r")
inputted_file=file.read().split()

inputted_file=[int(i) for i in inputted_file]
k=inputted_file[0]
array=inputted_file[1::]
out= str(find_k(array, 0, len(array)-1,k-1))
output= open("output5b.txt", mode="w")
output.write(out)
output.close()
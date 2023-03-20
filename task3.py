
f=open("input3.txt","r")
f1=open("output3.txt","w")

s1 = f.readline()
s1= s1.rstrip('\n')
s2 = f.readline()
s2= s2.rstrip('\n')
s3 = f.readline()

def LCS(X, Y,Z):    
    m = len(X) + 1
    n = len(Y) + 1
    o = len(Z) + 1
    if m >= 100 or n >= 100 or o >=100:
        return -1
    
    c = [[[0 for z in range(o)] for y in range(n)] for x in range(m)]
    
    for i in range(m):
        for j in range(n):
            for k in range(o):
                if i== 0 or j== 0 or k== 0:
                    c[i][j][k] = 0
                     
                elif X[i-1] == Y[j-1] and X[i-1] == Z[k-1]:
                    c[i][j][k] = 1+ c[i-1][j-1][k-1]
 
                else:
                    c[i][j][k] = max(max(c[i-1][j][k],c[i][j-1][k]),c[i][j][k-1])
    
    print(c[m-1][n-1][o-1])
    f1.write(str(c[m-1][n-1][o-1]))

final= LCS(s1,s2,s3)

f.close()
f1.close()
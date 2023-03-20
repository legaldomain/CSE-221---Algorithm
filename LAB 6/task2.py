f=open("input2.txt","r")
f1=open("output2.txt","w")

q= int(f.readline())
r= f.readline()
s1= f.readline()
Dict = {'Y': 'Yasnaya', 'R': 'Rozhok', 'S':'School', 'P':'Pochinki', 'F':'Farm', 'M':'Mylta', 'H':'Shelter', 'I':'Prison'}

def LCS(X, Y):    
    m = q + 1
    n = q + 1
    c = [[0 for x in range(n)] for y in range(m)]
     
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                c[i][j] = 0
                
            elif X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
    #print(c)            
    index = c[m-1][n-1]
    
    t = [""] * (index)
    l = m-1
    u = n-1
    while l > 0 and u > 0:

        if X[l-1] == Y[u-1]:
            t[index-1] = X[l-1]
            l = l-1
            u= u-1
            index = index-1

        elif c[l-1][j] > c[l][u-1]:
            l = l-1
        else:
            u= u-1
            
    for k in t:
        for key,value in Dict.items():
            if k==key:
                print(value, end=' ')
                f1.write(value)
                if k!=t[index-1]:
                    f1.write(' ')
                
    Correctness = (len(t) * 100)// q
    print('\n')
    f1.write('\n')
    print('Correctness of prediction: '+ str(Correctness)+ '%')
    f1.write('Correctness of prediction: '+ str(Correctness)+ '%')

final= LCS(r,s1)


f.close()
f1.close()
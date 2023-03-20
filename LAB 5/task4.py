f=open("input4.txt","r")
f1=open("output4.txt","w")

for line in f:
    count = 0
    l=line
    if l =='0 0':
        break
    else:
        val= list(map(int, l.split()))
        start= val[0]
        end= val[1]
        if start<=0 or end>100000:
            break
        for i in range(start, end + 1):
            if int(i ** 0.5) == i ** 0.5:
                count += 1
        #print(count)
        f1.write(str(count))
        f1.write('\n')
        
f.close()
f1.close()
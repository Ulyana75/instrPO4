for i in range(34526,167623):
    d=[]
    if int(i**(1/2))==i**(1/2):
        d.append(int(i**(1/2)))
    else:
        continue
    for j in range(2,int(i**(1/2))):
        if i%j==0:
            d.append(j)
            d.append(i//j)
        if len(d)>5:
            break
    if len(d)==5:
        d.sort()
        print(d)

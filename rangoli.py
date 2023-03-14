size = int(input())
lst = []
alp = "abcdefghijklmnopqrstuvwxyz"
st=""
alp1 = alp[:size]
for i in range(1,size+1):
    st = (alp1[-i:])
    lst.append(st)
lst1 = []
lst1.append(lst[0])
for i in range(len(lst)-1):
    temp=""
    x = lst[i+1]
    if len(x)>1:
        for j in x:
            temp = j + temp
    lst1.append(temp+lst[i])
lst2= []
for i in range(len(lst1)-2,-1,-1):
    lst2.append(lst1[i])

lst1.extend(lst2)
for i in lst1:
    lene = len(i)
    if len(i)<(4*size-3):
        for j in range(int((4*size-3-lene)/2)):
            i="-"+i
        for j in range(int((4*size-3-lene)/2)):
            i=i+"-"
        
    print(i)

    

    
    
    

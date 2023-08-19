def insertionsort(l):
    for i in range(1,len(l)):
        temp=l[i]
        j=i-1
        while(j>=0 and l[j]>temp):
            l[j+1],l[j]=l[j],l[j+1]
            j=j-1
 
    return l

a=[5,34,66,23,21,12,28]
a=insertionsort(a)
print(a)


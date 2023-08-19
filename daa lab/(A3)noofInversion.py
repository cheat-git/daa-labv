#countinginversion
def merge(a,b):
    i=0
    j=0
    co=0
    while(i<len(a) and j<len(b)):
        if a[i]<=b[j]:
            i+=1
        else:
            co+=(len(a)-i)
            j+=1
    return co
user1=[8,1,4,5,6,2,7,3]
user2=[1,2,3,4,5,6,7,8]
user3=[5,3,2,4,1,8,7,6]
a=[]
a.append(merge(user2,user1))
a.append(merge(user3,user1))
if a[0]<a[1]:
    print("user 2 recommends to user 1")
elif a[0]>a[1]:
    print("user 3 recommends to user 1")
else:
    print("Both users can recommends to user 1")
a=[]
a.append(merge(user1,user2))
a.append(merge(user3,user2))
if a[0]<a[1]:
    print("user 1 recommends to user 2")
elif a[0]>a[1]:
    print("user 3 recommends to user 2")
else:
    print("Both users can recommends to user 2")
a=[]
a.append(merge(user1,user3))
a.append(merge(user2,user3))
if a[0]<a[1]:
    print("user 1 recommends to user 3")
elif a[0]>a[1]:
    print("user 2 recommends to user 3")
else:
    print("Both users can recommends to user 3") 
    
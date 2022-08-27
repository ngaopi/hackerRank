list=[1,2,3,4,5,6]
user=int(input("enter the number:-"))
a=[]
i=0
while i<len(list):
    j=0
    while j<len(list):
        if list[i]+list[j]==user and list[i]<list[j]:
            c=i,j
            a.append(c)
        j=j+1
    i=i+1
print(a)
                      
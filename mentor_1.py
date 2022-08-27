#list=["12","89",88,55]
# i=0
# sum=0
# while i<len(list):
#     if list[i]==str(list[i]):
#         x=int(list[i])
#         sum+=x 
#     else:
#         sum+=list[i]
#     i=i+1
# print(sum)

# l=list(map(int,input().split()))
# print(l)

l=[[1,3,4],[5,3,7],[9,2,6]]
i=0
b=[]
while i<len(l):
    j=0
    while j<len(l[i]):
        b.append(l[i][j])
        j=j+1
    i=i+1
k=0
while k<len(b):
    x=k+1
    while x<len(b):
        if b[k]>b[x]:
            b[k],b[x]=b[x],b[k]
        x+=1
    k+=1
print(b)
    

                  

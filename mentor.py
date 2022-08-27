# list=[2,1,3,6,5,4,9]
# i=0
# a=[]
# while i<len(list):
#     c=0
#     j=0
#     b=[]
#     while j<len(list) :
#         if list[i]<list[j]:
#             c=c+1
#         j=j+1
#     b.append(list[i])
#     b.append(c)
#     if b not in a:
#         a.append (b)
#     i=i+1
# print(a)

list=[2,1,3,6,5,4,9]
i=0
a=[]
while i<len(list):
    c=0
    j=0
    while j<len(list) :
        if list[i]<list[j]:
            c=c+1
        j=j+1
    a.append(c)
    i=i+1
print(a)
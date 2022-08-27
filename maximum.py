n=int(input("enter the number:-"))
s=[]
y=[]
i=0
while i<n:
    x=[]
    name=input("name")
    score=float(input("score"))
    x.append(name)
    x.append(score)
    y.append(x)
    s.append(score)
    i+=1
s.sort()
b=s[1]
for i,j in y:
    if j==b:
        print(i)

def split_and_join(line):
    b=[]
    for i in range(len(line)):
        c=line.split()
        d="-".join(c)
    return d
print(split_and_join(line="I love the way you are"))
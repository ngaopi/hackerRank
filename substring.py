def count(string,sub_string):
    c=0
    n=len(sub_string)
    for i in range(len(string)):
        if string[i:n]==sub_string:
            c=c+1
        n+=1
    return c 
print(count(string="ABCDCDC",sub_string="CDC"))

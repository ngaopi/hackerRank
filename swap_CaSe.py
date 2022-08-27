def main(s):
    b=[]
    for i in range(len(s)):
        if (s[i].isupper())==True:
            b.append(s[i].lower())
        elif (s[i].islower()==True):
            b.append(s[i].upper())
        else:
            b.append(s[i])
        stri=''
    return stri.join(b) 
print(main(s="RingNiM"))
    

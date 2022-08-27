# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.
def plusMinus(arr):
    c,d,e=0,0,0
    i=0
    while i<len(arr):
        if arr[i]<0:
            c=c+1
        elif arr[i]>0:
            d+=1
        else:
            e+=1
        j,k,l=d/len(arr),c/len(arr),e/len(arr)
        i=i+1
    print(j)
    print(k)
    print(l)
plusMinus([1, 2 ,3, -1 ,-2 ,-3 ,0 ,0])

                        
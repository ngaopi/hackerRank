# def staircase(n):
#     l=int(input("enter the number:-"))
#     i=1
#     while i<=n:
#         j=1
#         while j<=l:
#             print(" ",end="")
#             j=j+1
#         k=1
#         while k<=i:
#             print("#",end="")
#             k=k+1
#         print()
#         l=l-1
#         i=i+1
# staircase(n=int(input("enter the number:-")))

def staircase(n):
    for i in range(1,n+1):
        print(("#"*i).rjust(n," "))
staircase(n=int(input("enter the number:-")))
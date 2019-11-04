l,# def fact(x):
#     if x==0:
#         return 1
#     else:
#         return x*fact(x-1)
# x=4
# print(fact(x))
#
# def fact(x):
#     if x==0:
#         return 1
#     else:
#         return x*fact(x-1)
# x=4
# print(fact(x))

def fact(x):
    print("The factorial of",x,"are:")
    for i in range(1,x+1):
        if x%i==0:
            print(i)
num=30
print(fact(num))

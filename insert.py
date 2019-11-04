# def add(x,y):
#     return x+y
# sum=add(3,4)
# print(sum)

# def multiply_list(items):
#     tot=3
#     for i in items:
#         tot*= i
#     return tot
# print(multiply_list([1,2,-8]))


# def max_num_list(list):
#      max =list[0]
#      for i in list:
#          if i >max:
#              max = i
#      return max
# print(max_num_list([1,2,3,4,5]))
#
#
# # largest number
# list=[1,2,3,4]
# max=list[1]
# for i in list:
#     if  i > max:
#         max=i
# print(max)


# smallest number
# def smallest(list):
#     min= list[0]
#     for i in list:
#         if min > i:
#             min =i
#     return min
# print(smallest([1,2,3,4]))

# def maths_word(words):
#     count=0
#     for i in words:
#         if len(i)>1 and i[0]==i[-1]:
#             count +=1
#     return count
# print(maths_word(['abc','xyz','aba',1221]))

list=['abc','xyz','aba',1221]
count=0
for i in list:
    count=count+1
print("lenth of the string is:",count)
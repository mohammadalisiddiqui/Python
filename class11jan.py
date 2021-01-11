# for x in range(1,6):
#     print("*")

# for x in range(1,6):
#     print("*",end="")


# for y in range(1,6):
#     for x in range(1,6):
#         print("*",end="")
#     print("")

# for x in range(1,6):
#     for b in range(0,x):
#         print("*",end="")
#     print("")    

# for x in reversed(range(1,6)):
#     for y in range(0,x):
#         print("*",end="")
#     print("")

import numpy as np

# a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(a)
# x = np.split(a,6) # to split equally
# print(x)
# # x = np.array_split(a,5)  #to split unequally
# print(x)

# arr2 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# print(arr2)
# print(arr2.ndim)

# # a = np.split(arr2,2)
# # print(a)

# # a = np.array_split(arr2,4,axis=1)
# # print(a)
# b = arr2.reshape(-1)
# print(b)
# c = b.reshape(4,4)
# print(c)

# y = np.split(c,4,axis=1)
# print(y)

# new_arr = np.array([[range(1,5)],[range(5,9)],[range(9,13)],[range(13,17)]])
# print(new_arr)
# a = new_arr.reshape(-1)
# b = a.reshape(4,4)
# print(b)

# new_arr2 = np.array([[range(1,5)],[range(5,9)],[range(9,13)],[range(13,17)]])
# print(new_arr)
# a2 = new_arr.reshape(-1)
# b2 = a2.reshape(4,4)
# print(b2)

# st = np.hstack((b,b2))
# print(st)

# vst = np.vstack((b,b2))
# print(vst)

# important task

arr3_d = np.array([range(1,28)])

a = arr3_d.reshape(3,3,3)
print(a)

x = np.split(a,3,axis =2)
print(x)



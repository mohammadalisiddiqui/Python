# import numpy
# arry = numpy.array([1,2,3,4])
# print(arry)

# import numpy as rp
# arry = rp.array([5,4,6,3])
# print(arry)

# print(rp.version) #give version of library

# import numpy as rp

# arry = rp.array([[44,55,44],[66,4,5]])
# print(arry)
# print(arry[0,1])

# arry = rp.array([[[4,3,1],[5,4,6],[9,8,7]],[[4,3,1],[5,4,6],[9,8,7]],[[4,3,1],[5,4,6],[9,8,7]]])
# print(arry)
# print(arry[2,2])
# print(arry[0:])

# arry = rp.array([1,2,3,4,5,6,7,8,9])
# print(arry[0:6:1])
# print(arry[::2])


                # Practice

import numpy as np
arry = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]],[[19,20,21],[22,23,24],[25,26,27]]])
print(arry)
print("indexing in array")
print(arry[1,2,2])
print(arry[0,1])
print(arry.size)
print()
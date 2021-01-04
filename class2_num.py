import numpy as np
# my_array = np.array(["Ali","AHmed","Adil","Omer"])
# print(my_array)
# print(my_array.dtype)

# arr = np.array([1,2,3])
# print(arr.dtype)

# c = np.array([1,2,3,4,5], dtype='S')
# # print(c)
# print(c.dtype)

# d = np.array(["a",2,9], dtype="i")
# print(d.dtype)



# arr = np.array([2.66,6.99,5.3,3.2], dtype="f")
# print(arr.dtype)
# print(arr)
# print(type(arr))
# x = arr.astype(int)
# print(x.dtype)


# arr = np.array([0.00,6.99,5.3,3.2,-12.3], dtype="f")

# x = arr.astype(bool)
# print(x)


# arr = np.array([0.00,6.99,5.3,3.2,-12.3], dtype="f")

# d = arr.view()   #d is not itself array it is only view array of name arr
# d[0] = 1.32
# print(arr)
# print(d)
# print("base")
# print(d.base)  #By using base command we verify our variable dependent or not
# print("\t copy environment")
# d = arr.copy()
# d[0] = 4.55
# print(arr)
# print(d)

# print(d.base)



# new_array = np.array([[1,6],[7,5],[3,2]])
# print(new_array)
# print(new_array.shape) #shape return size of matrix e.g row and column


# new_array = np.array([1,2,3,4,5], ndmin=3)  #ndmin is use for create dimension
# print(new_array)
# print(new_array.shape)
# print(new_array.ndim)
# print(new_array[:,:,4])

# new_array = np.array([1,2,3,4,5,6,7,8,9])
# print(new_array)
# new_array = new_array.reshape(3,3)  #2 dimension array
# print(new_array)
# print(new_array.shape)
# print(new_array.ndim)

# new_array = np.array([1,2,3,4,5,6,7,8])
# print(new_array)
# new_array = new_array.reshape(2,2,2)
# w = new_array.reshape(-1)
# print(new_array)
# print(new_array.shape)          #platning is a process any dimension of metrix can convert in one dimension matrix
# print(new_array.ndim)

# print("\tplatring")
# print(w)
# print(w.shape)
# print(w.ndim)

# print(np.array([1,2,3,4,5,6,7,8,9,10]))
# print(np.array(range(1,101)))

a = np.array(range(1,101))
b = a.reshape(5,5,4)
print(b)

for x in b:
    if x%2 == 0:
        print(x)
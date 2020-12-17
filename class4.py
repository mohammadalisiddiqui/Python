                            # class 4 17 dec 2020

# fresh = ["Apple","Banana","Cherry","Mango","Appricot","Orange"]
# # if fresh[3]=="Mango" in fresh:
# #     print("available")

# # for i in range(len(fresh)):
# #     print(i)
# # for i in fresh:
# #     print(i)

# i =0
# while i<len(fresh):
#     print(fresh[i])
#     i=i+1

# z = ["Mango","Orange","Apple","Strawberry","Watermelon"]
# new= [x for x in z if "o" in x]
# print(new)

# new= [x for x in z if "pp" in x]
# print(new)

# new= [x for x in z if x!="Apple"]
# print(new)

                    #tuple

w = ("watermelon",2,"apple","Orange","pineapple")
print(type(w))
# z = input("Enter fruit name")
# if z == "watermelon" or z== 2 or z=="apple" or z== "Orange":
#     print(z+" is available in tuple")
# else:
# print(z+" is not available in tuple")

# c = list(w)
# c[0] = "mango"
# print(c)
# w = tuple(c)
# print(w)

x =  ("Apple","Banana","peach")

# a,b,c = x
# print(a)
# print(b)
# print(c)

# a,b = x
# print(a)
# print(b)  #give error

a,*b = x
print(a)
print(b)



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

# z = ["Mango","orange","Apple","Strawberry","Watermelon"]
# new= [x for x in z if "o" in x]
# print(new)

# new= [x for x in z if "pp" in x]
# print(new)

# new= [x for x in z if x!="Apple"]
# print(new)

                    #tuple

# w = ("watermelon",2,"apple","Orange","pineapple")
# # print(type(w))
# z = input("Enter fruit name")
# if z== "watermelon" or z== 2 or z=="apple" or z== "Orange" or z=="Pineapple":
#     new= [x for x in w if x==z]
#     a = list(new)
#     a = str(new)
#     print(a+" is available in tuple")
# else:
#     new= [x for x in w if x!=z]
#     print(z+" is not available in tuple")

# c = list(w)
# c[0] = "mango"
# print(c)
# w = tuple(c)
# print(w)

# x =  ("Apple","Banana","peach")

# a,b,c = x
# print(a)
# print(b)
# print(c)

# a,b = x
# print(a)
# print(b)  #give error

# a,*b = x
# print(a)
# print(b)

            # practice

# tple = ("Ali",2,"mango","pineapple")
# x = ("Peach","Orange")
# # tple.append()
# # tple.pop(7)
# # tple.extend(x)
# print(tple)

            # 18 Dec 2020

# tple = ("Ali",2,"mango","pineapple","orange","peach")

# for i in tple:
#     print(i)

# for i in range(len(tple)):
#     print(tple[i])

# a = 0
# while a<len(tple):
#     print(tple[a])
#     a=a+1

# a = tple * 2
# print(a.count("mango"))
# print(a.index("mango"))

# set_1 = {"ali","iqbal","jawad","fayyaz","owais","moben","fahad"}
# print(set_1)
# print(len(set_1))
# set_2 = {"ali","ahad","tanzel","owais"}
# print(set_2)

# # find = {x for x in set_1 if "ali" in x }
# # print(find)
# # set_1.add("Erdum") #add erdum at random index number
# # print(set_1)
#     # set_1.append("khizar") give error beacuse set has no attribute append
#     # print(set_1)

# set_1.update(set_2)
# print(set_1)

# list_1 = ["mango","apple"]

# set_1.update(list_1) # ad list and set as a set type
# print(set_1)

# set_1.remove("iqbal")
# print(set_1)

# # set_1.remove("iqbal") #give error beacuse iqbal has already remove
# # print(set_1)

# set_1.discard("ahad") #dicard does not show error if element has already remove
# print(set_1)

# new_set = {"mango","apple","orange","lemon","pineapple"}
# new_set2 = {"apple","orange"}
# z = new_set.intersection(new_set2)
# print(z)

                                        # dictionary

set_4 = {"Daniyal"}
dict_1 = {"A":"Ali","B":"Bilal","C":"Chandio","D":set_4}

print(type(dict_1))

print(dict_1["A"])
print(dict_1["B"])
print(dict_1["C"])
print(dict_1["D"])
print(dict_1)

print(len(dict_1))

print(dict_1)

print(dict_1.keys())

print(dict_1)
dict_1["D"] = "Dawood" # add new key
print(dict_1)

if  "B" in dict_1:
    print(dict_1["B"])

# a = input("Enter your Key")
# if a=="A" or a=="B" or a=="C" or a=="D":
#     print(dict_1[a])
# else:
#     print("your key value not in dictionary")

dict_1.pop("C")
print(dict_1)

new_dict = {"A":"Ali","B":{"Bu":"Butter","Ba":"Ball"},"C":"cocunut"}
print(new_dict["B"]["Bu"])
                                # 21 Dec 2020

# a = 3
# b = 2
# if b>a:
#     pass

# x = int(input("enter number"))
# y = x%2
# if y==0:
#     print("given number is Even")
# elif y==1:
#     print("given number is Odd")

# i = 1 
# while i <6:
#     print(i)
#     if i==3:  # in a break statement loop will break
#         break
#     i+=1

# i = 0
# while i <6:
#     i+=1
#     if i==3:  
#         continue
#     print(i)

# i = 1 
# while i <6:
#     print(i)
#     i+=1
# else:
#     print("i is no longer less tahn 6")

# i=0
# while i <6:
#     i+=1
#     if i==3:  
#         pass
#         # print("ali")
#     print(i)

# fruit = ["apple","mango","banana","appricot","cherry"]
# for x in fruit:
#     if x =="appricot":
#         break
#     print(x)

# i = 0
# while i < len(fruit):
#     print(fruit[i])
#     i +=1
#     if fruit[i]=="appricot":
#         break
    
                        # function

# def my_func(a,b):
#     c = a+b
#     print("the sum of a and b is =",c)
# num1 = int(input("enter value of a"))
# num2 =int(input("enter value of b"))
# my_func(num1,num2)

# def name(*value):
#     print("my name is" + value[3])
# name("ali","ahad","ahmed","owais")

# def names(nam,fnam):
#     print("my name is" + fnam)
# names(nam = "Ali", fnam = "Mehfooz Ali")

# def names(nam = "Ali"):
#     print("my name is" + nam)
# names()


# def bas(fruit):
#     for x in fruit:
#         print(x)    
# items = ["Apple","Mango","Cherry","dates"]
# bas(items)

# def bas(fruit):
#     for x in fruit:
#         if x=="Cherry":
#             print(x)
#             break
#         print(x)    
# items = ["Apple","Mango","Cherry","dates"]
# bas(items)

# def sum(v1,v2):
#     add = v1+v2
#     return add
# num1 = int(input("enter value of a"))
# num2 =int(input("enter value of b"))
# x = sum(num1,num2)-4
# print(sum(num1,num2))
# print(x)

# def max(v1,v2):
#     if v1>v2:
#         txt = "The value of a={0}is greater than b={1}"
#         print(txt.format(v1,v2))
#     elif v2>v1:
#         txt = "The value of b={0}is greater than a={1}"
#         print(txt.format(v2,v1))
#     elif v1==v2:
#         txt = "value of a={0} = value of b={1}"   
#         print(txt.format(v1,v2)) 
# num1=int(input("enter value of a"))
# num2=int(input("enter value of b"))
# max(num1,num2)


# def bas():
#     while(True):
#         ui = input("Enter fruit name \n")
#         if ui=="Cherry":
#             print(ui)
#             break

# bas()

                                        # 22 Dec 2020


# def max_num(*args):
#     print("the highest num is = ",max(args)) #give back the highest number
#     print("the minimum num is = ",min(args)) #give back the lowest number
# num1=int(input("enter value of a"))
# num2=int(input("enter value of b"))
# num3=int(input("enter value of c"))
# max_num(num1,num2,num3)





# def add(*args):
#     i=0
#     while i<len(args):
#         c =args[i]
#         print(args)
#         num = c
#         res = 0
#         res += num
#         i+=1
#         print(res)
# add(my_list)   


# my_list = [2,5,6,4,9,5]
# def addition(my_list):
#     add = sum(my_list)                  # add all list values
#     print("the sum is =",add)
# addition(my_list)



# def ran():
#     while(True):
#         val = int(input("enter any number"))
#         c = range(11)
#         if val in c:
#             print("yes number is available in list")     #take input from user and if it is range from0,10
#             break                                        # show yes otherwise not
#         else:
#             print("number is not available")
#             continue
            
# ran()

# def f1(x,y):
#     if x>y:
#         return x
#     return y                  # give back highest value
# def f2(x,y,z):
#     return f1(x,f1(y,z))
# print(f2(3,6,11))

def revst():
    name = input("enter any string")
    c = name
    print(c.reverse())
revst()





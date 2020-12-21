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


def bas():
    while(True):
        ui = input("Enter fruit name \n")
        if ui=="Cherry":
            print(ui)
            break

bas()
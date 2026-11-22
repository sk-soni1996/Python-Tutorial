
# lazy import os
# lazy import datetime




# def greet(name:str) -> str:
#     return f"Hello! {name}."

# # print(greet("Soni"))
# a=10
# b=5
# print(a+b)
# print(a//b)
# print(a/b)
# s1 ="Hello"
# s2 ="World"
# s3 = 4
# print(s1+s2)
# print(s1*4)

# #Relational operator
# s1=121
# s2=141

# print(s1>s2)
# print(s1<s2)
# print(s1>=s2)
# print(s1<=s2)

# a1= "HELLO"
# a2="WORLD"
# a3="Hello"


# print(a1>a2)
# print(a1<a2)
# print(a1>=a2)
# print(a1<=a2)

# #Logical Operators -- and , or , not 
# # and -- if bpth arguments are true result is true
# # or -- if anyone argument  is true result is true 
# # not -- compliment
# print("------------------")
# print("" and "")
# print("BG" and "OG")
# print("BG" and "")

# print("-------or-----------")

# print("" or "")
# print("BG" or "OG")
# print("BG" or "")

# print("-------not-----------")

# print(not "")
# print(not "OG")
# print(not "BG")
# print(not 0)
# print(not 10)

# #bitwise operator : & , | , ^ , ~ ,<< , >>

# print("BG" and "OG")

# # Assignment Opertor 

# # = Assinment , == (Comparrision)

# x=10
# y=100
# print(x==y)
# print(x!=y)

# x+=100 # x=x+100 -- x=10
# print(x)

# #Ternary operator
# # syntax -- x= first value if condition else second value 

# z1=100
# z2=420
# z5=600

# z3 = z1 if z1>z2 else z2
# print(z3)

# z4 = z1 if z1<z2 else z2
# print(z4)

# z6= z1 if z1>z2 and z1>z5 else z2 if z2>z5 else z5
# print(z6)

# #Opposite condition to get lowest value 
# z6= z1 if z1<z2 and z1<z5 else z2 if z2<z5 else z5
# print(z6)

# #Opposite Variable to get lowest value

# z6= z5 if z2<z1 and z5<z1 else z1 if z5<z2 else z1
# print(z6)


# #Special Operator
# #1. Membership operator : in and not in
# #2. Identity operator : is and is not ( we use for address comparison)

# a=10
# b=10
# c=20

# print(a is b)
# print(b is c)
# print(a is not c)

# num = input("enter number to chekc : ")
# print(f"{len(num)} digit number")

# num = 56342
# test = num
# count = 0
# new_num = 0
# while num > 0:
#     digit = num % 10
#     new_num = new_num*10 + digit
#     # count += 1
#     num = num//10
# # print(f"{count} digit number")
# print(test)
# print(new_num)

# num = 2202
# print(abs(num))

# st = 'python'
# # for i in range(len(st)-1, -1, -1):
# #     print(st[i], end='')
# # print(st[6])
# # for i in st:
# #     print(i)
# # print('=')
# for i in range(len(st)):
#     print(i)
#     print(f"value = {st[i]} and index = {i}")

# for i in range(0,11):
#     print(i*2)

# for i in range(1,101):
#     if i%2==0:
#         print("this is a even number",i)


# print([i for i in range(1, 100) if i%2==0])

# x= 100
# print(100)
# print(type(x))
# print(eval("10+20"))


# def wish(name):
#     print("Good morning",name)
#     print("How are you")
# wish("name")    --- iwanted pass soni instead of name

# def factorial(n=5):
#     if n==0:
#         return 1
#     else:
#         return (n*factorial(n-1))
# print(factorial(3))
# print(factorial())

# def greet(age, name="Soni"):
#     print(age)
#     print("Hello ", name)

# greet(30)    
# greet(35,"Sachin")
    
    
# def sum(*args):
#     print(args)
#     sm = 0
#     for i in args:
#         sm += i
#     return sm

# print(sum(1,2,3,4,5,6))
# print(sum(19,20,30))
# print(sum(19))

# def x(int):
#     print(int+2)
#     return x
# x(65)

# def add(x,y):
#     # print(x+y)
#     return(x+y)

# print(add(6,8))
# # result =add(6,8)
# # print(result) 

# def myfuncnction():
#     print("helo world")
#     return 3+3
#     print("helo world")
# print(myfuncnction())

# x = lambda a, b, c : a+b+c
# print(x(5,6,7))


# x = ["apple", "banana","Cherry"]
# y=x
# print(y is x)


# def even():
#     num = int(input("Enter a number"))
#     if num%2==0:
#      print("This is even number")
#     else:
#        print("This is odd number")

# even()

# thislist = ["Soni","Mamta","Sntoshi"]
# print(thislist)
# thislist[2] ="Babita"
# print(thislist)
# thislist[1:3] = ["Dimple","OM"]
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# print(thislist[:])
# thislist[:] = ["blackcurrant", "watermelon"]
# print(thislist)
## lIST FUNCTIONS
"""
LIST FUNCTIONS
1. append()
2. extends()
3. replace()
4. reverse()
5. sort()
6. sorted()
7. pop()
8. index()
"""

# curr_lst = [1,2,3,4]
# print(curr_lst)
# curr_lst.append(10)
# print(curr_lst)
# curr_lst.extend([20,30,40])
# print(curr_lst)
# curr_lst.insert(3, 100)
# print(curr_lst)
# print(curr_lst.pop(3))
# print(curr_lst)
# curr_lst.remove(10)
# print(curr_lst)
# curr_lst.sort(reverse=True)
# print(curr_lst)
# new_lst=sorted(curr_lst, reverse=True)
# print(new_lst)
# print(new_lst.index(30))


from random import *

# for i in range(10):
#     print(randrange(10))
# print("------------------------------")    


# for i in range(100):
#     print(randrange(1,10))
# print("------------------------------")  

# for i in range(100):
#     print(randrange(0,99,5))


d = {}
n=int(input("Enter the numbersof  student :"))
i=1
while i<=n:
    name = input("Enter the student name ")
    marks = int(input("enter student marks "))
    d[name]=marks
    i= i+1
    print("name of the stude ")
    print(d)



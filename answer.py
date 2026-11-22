"""Check whether a number is Even or Odd."""
num = int(input("Enter a Number"))
if num%2 == 0:
    print("Even")
else:
    print("Odd")



""" Check whether a number is Positive, Negative, or Zero."""

if num>0:
    print("positive")
elif num<0:
    print("Negative")    
else:    
    print("Zeo")




"""Find the largest of two numbers."""


num1 = int(input("Enter The first number"))
num2 = int(input("Enter the second number"))
if num1>num2:
   print(f"{num1} Greater")
else:
  print(f"{num1} Smaller") 


"""Find the largest of three numbers."""    

num1 = int(input("Enter The first number"))
num2 = int(input("Enter the second number"))
num3 = int(input("Enter the third number"))
if num1>num2 and num1>num3:
    print(f"{num1}is Greater")
elif num2>num1 and num2>num3:
    print(f"{num2} is Greater")    
else:
    print(f"{num3}is Greater")  



    
"""Check whether a person is eligible to vote."""
age= int(input("Enter the Age"))

if age>17:
    print(f"{age} You are eligible to Vote")
else:
      print(f"{age} You are not eligible to Vote")    

"""Check whether a given year is a Leap Year."""    
year= int(input("Enter Year"))

if year % 400 == 0:
    print(f"{year}Leap")
elif year % 100 ==0:
    print(f"{year}notLeap")
elif year % 4==0: 
    print(f"{year}Leap")    
else:    
    print(f"{year}NotLeap")  


"""Calculate grade based on marks entered by the user."""    
grade=int(input("Enter the marks"))
if grade>75 and grade<=100:
    print(f"{grade}Belongs to A grade")
elif grade >55 and grade<=75:
    print(f"{grade}Belongs to B grade")
else:
     print(f"{grade}Belongs to c grade")


"""Check whether a character is a Vowel or Consonant."""


v1= input("Enter the word")

if v1 in "aeiou" or v1 in "AEIOU":
    print(f"{v1} it's Vowel")

else:
    print(f"{v1} it's Consonant")


"""Verify a password entered by the user."""

v1= input("Enter the word")
if v1== "":
    print(f"{v1} Password is empty")
else:
    print(f"your password is: {v1} ")


    """Calculate discount based on purchase amount."""

    amt=int(input("Enter Amount"))
if amt>=5000: 
    print(f"{amt-amt*0.15} you got discont of 15%")
elif amt>=1500 and amt <5000:  
    print(f"{amt-amt*0.10} you got discont of 10%")
else:
    print(f"{amt-amt*0.05} you got discont of 5%")


"""Check whether a number is divisible by 5 and 11."""

div = int(input("Enter the Number"))
if div % 5 == 0 and div % 11 == 0: 
    print(f"{div} is divisible by 5 and 11")  
else:
   print(f"{div} is not divisible by 5 and 11")



"""Check whether a number is a multiple of 3."""

mul = int(input("Enter the Number"))
if mul % 3==0:
     print(f"{mul} is Multiple by 3") 

else:
     print(f"{mul} is not Multiple by 3") 



"""Find the smallest of three numbers."""

n1=int(input("Enter 1st number"))
n2=int(input("Enter 2nd number"))
n3=int(input("Enter 3rd number"))
if n1<n2 and n1<n3:
   print(f"{n1}is Smaller")
elif n2<n1 and n2<n3:
   print(f"{n2}is smaller") 
else:
   print(f"{n3}is smaller")  

   """Check whether a character is an Alphabet, Digit, or Special Character."""
   x = input("Enter the char")
if x.isalpha():
    print("Its an alphabet")
elif x.isdigit():
    print("It's a digit")
else:
    print("it is a special character")    
